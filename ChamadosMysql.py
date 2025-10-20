from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ConversationHandler, ContextTypes, CallbackQueryHandler
)
from datetime import datetime
from config_bot_ChamadoBFF import TELEGRAM_TOKEN, ADMIN_PASSWORD, TECNICO_RESPONSAVEL_ID
import random
# Remova o import do sqlite3 e adicione:
import mysql.connector
from mysql.connector import Error
from config_bot_ChamadoBFF import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

async def definir_comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_my_commands([
        ("start", "Iniciar o bot"),
        ("ajuda", "Mostrar ajuda"),
        # Adicione outros comandos conforme necessário
    ])



# 1. Defina a timezone (se não estiver já)

import pytz
from telegram.ext import ApplicationBuilder

# Crie a aplicação
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# ⚙️ Configure o JobQueue com pytz (ESSENCIAL)
app.job_queue.scheduler.configure(timezone=pytz.timezone('America/Sao_Paulo'))



#Estados da conversa
SETOR, ALA, LOCALIDADE, PATRIMONIO, TIPO, DESCRICAO = range(6)
SOL_SENHA, SOL_ID, SOL_TEXTO = range(6, 9)


# Listas
EQUIPAMENTOS = ["💻 Computador", "📱 Notebook", "🖨️ Impressora", "🔧 Outros"]
SETOR_LISTA = [
        "👩‍💼 Chefia Técnica da BFF",  # Diretora da Biblioteca
        "📝 Secretaria",             # Mantive, parece condizer
        "🤝 SAU",                    # Serviço de Atendimento ao Usuário
        "🛠️ Oficina",                # Mantive, parece condizer
        "📚 PCD",                    # Produção Científica e Docente
        "⚙️ SAT",                    # Serviço de Apoio Técnico
        "📖 STL",                    # Serviço Técnico de Livros
        "↔️ SAI",                    # Serviço de Aquisição e Intercâmbio
        "🧹 Zeladoria",              # Mantive, parece condizer
        "🔑 Chaves"                  # Mantive, parece condizer
    ]
ALA_LISTA = ["🏢 Ala Nova", "🏛️ Ala Antiga"]
LOCALIDADE_LISTA = ["🏬 Subsolo", "🏪 Térreo", "1️⃣º Andar", "2️⃣º Andar"]


# Função para conexão com o MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


# Banco de dados
# Modifique todas as funções do banco de dadas
def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chamados (
                id VARCHAR(20) PRIMARY KEY,
                data_hora VARCHAR(50) NOT NULL,
                nome VARCHAR(100) NOT NULL,
                user_id VARCHAR(50),
                setor VARCHAR(100) NOT NULL,
                ala VARCHAR(100) NOT NULL,
                localidade VARCHAR(100) NOT NULL,
                patrimonio VARCHAR(100) NOT NULL,
                tipo VARCHAR(100) NOT NULL,
                descricao TEXT NOT NULL,
                status VARCHAR(20) DEFAULT 'Aberto',
                solucao VARCHAR(255) DEFAULT ''
            )
        ''')
        conn.commit()
        conn.close()

def salvar_chamado(chamado_data):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO chamados 
            (id, data_hora, nome, user_id, setor, ala, localidade, patrimonio, tipo, descricao, status, solucao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            chamado_data['id'], chamado_data['data_hora'], chamado_data['nome'], chamado_data['user_id'],
            chamado_data['setor'], chamado_data['ala'], chamado_data['localidade'], chamado_data['patrimonio'],
            chamado_data['tipo'], chamado_data['descricao'], 'Aberto', ''
        ))
        conn.commit()
        conn.close()

def buscar_chamado_por_id(chamado_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT descricao FROM chamados WHERE id = %s', (chamado_id,))
        row = cursor.fetchone()
        conn.close()
        return row[0] if row else None
    return None

async def atualizar_solucao_chamado(chamado_id, nova_solucao, application):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE chamados SET solucao = %s, status = 'Fechado' WHERE id = %s
        ''', (nova_solucao, chamado_id))
        conn.commit()
        cursor.execute('SELECT user_id FROM chamados WHERE id = %s', (chamado_id,))
        row = cursor.fetchone()
        conn.close()

        if row and row[0]:
            try:
                await application.bot.send_message(
                    chat_id=row[0],
                    text=f"✅ Seu chamado {chamado_id} foi resolvido e fechado!\n\n💡 Solução: {nova_solucao}"
                )
            except Exception as e:
                print(f"Erro ao notificar usuário: {e}")

# Comandos padrão
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá! Eu sou o bot de chamados.\n\n"
        "Use /chamado para registrar um problema.\n"
        "Use /solucao para resolver um chamado (admin).\n"
        "Use /cancelar para encerrar qualquer operação."
    )

async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Operação cancelada.")
    context.user_data.clear()
    return ConversationHandler.END

# Fluxo do chamado
async def iniciar_chamado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    context.user_data['nome'] = update.effective_user.full_name
    context.user_data['user_id'] = str(update.effective_user.id)
    teclado = [[InlineKeyboardButton(s, callback_data=s)] for s in SETOR_LISTA]
    await update.message.reply_text("🏢 Escolha o setor onde você trabalha:", reply_markup=InlineKeyboardMarkup(teclado))
    return SETOR

async def receber_setor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data['setor'] = update.callback_query.data
    teclado = [[InlineKeyboardButton(a, callback_data=a)] for a in ALA_LISTA]
    await update.callback_query.edit_message_text("🏢 Escolha a ala:", reply_markup=InlineKeyboardMarkup(teclado))
    return ALA

async def receber_ala(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data['ala'] = update.callback_query.data
    teclado = [[InlineKeyboardButton(l, callback_data=l)] for l in LOCALIDADE_LISTA]
    await update.callback_query.edit_message_text("📍 Escolha a localidade:", reply_markup=InlineKeyboardMarkup(teclado))
    return LOCALIDADE

async def receber_localidade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data['localidade'] = update.callback_query.data
    await update.callback_query.edit_message_text("📌 Informe o número do patrimônio do equipamento:")
    return PATRIMONIO

async def receber_patrimonio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['patrimonio'] = update.message.text
    teclado = [[InlineKeyboardButton(e, callback_data=e)] for e in EQUIPAMENTOS]
    await update.message.reply_text("🖥️ Qual o tipo de equipamento?", reply_markup=InlineKeyboardMarkup(teclado))
    return TIPO

async def receber_tipo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    context.user_data['tipo'] = update.callback_query.data
    await update.callback_query.edit_message_text(f"🖥️ Tipo: {context.user_data['tipo']}")
    await update.callback_query.message.reply_text("📝 Descreva o problema:")
    return DESCRICAO

async def receber_descricao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['descricao'] = update.message.text
    chamado = {
        "id": str(random.randint(10_000_000, 99_999_999)),
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "nome": context.user_data['nome'],
        "user_id": context.user_data['user_id'],
        "setor": context.user_data['setor'],
        "ala": context.user_data['ala'],
        "localidade": context.user_data['localidade'],
        "patrimonio": context.user_data['patrimonio'],
        "tipo": context.user_data['tipo'],
        "descricao": context.user_data['descricao']
    }
    salvar_chamado(chamado)
    await update.message.reply_text(
        f"✅ Chamado registrado com sucesso!\n🆔 ID: {chamado['id']}\n\nDeseja abrir outro? Use /chamado"
    )

    # Notifica o técnico responsável
    try:
        await context.application.bot.send_message(
            chat_id=TECNICO_RESPONSAVEL_ID,
            text=(
                f"📢 Novo chamado aberto!\n"
                f"👤 Nome: {chamado['nome']}\n"
                f"🆔 ID: {chamado['id']}\n"
                f"🏢 Setor: {chamado['setor']}\n"
                f"📍 Local: {chamado['ala']} - {chamado['localidade']}\n"
                f"🔢 Patrimônio: {chamado['patrimonio']}\n"
                f"📝 Problema: {chamado['descricao']}"
            )
        )
    except Exception as e:
        print(f"Erro ao notificar técnico: {e}")

    context.user_data.clear()
    return ConversationHandler.END

# Fluxo do comando /solucao
async def iniciar_solucao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text("🔐 Digite a senha de administrador:")
    return SOL_SENHA

async def receber_senha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text != ADMIN_PASSWORD:
        await update.message.reply_text("❌ Senha incorreta. Operação cancelada.")
        context.user_data.clear()
        return ConversationHandler.END
    context.user_data['autenticado'] = True
    await update.message.reply_text("✅ Senha correta!\n📄 Agora digite o ID do chamado:")
    return SOL_ID

async def receber_id_chamado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['id_chamado'] = update.message.text.strip()
    descricao = buscar_chamado_por_id(context.user_data['id_chamado'])
    if descricao:
        await update.message.reply_text(f"📝 Problema reportado:\n{descricao}\n\nAgora digite a descrição da solução:")
        return SOL_TEXTO
    else:
        await update.message.reply_text("❌ ID de chamado não encontrado. Operação cancelada.")
        context.user_data.clear()
        return ConversationHandler.END

async def receber_solucao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nova_solucao = update.message.text.strip()
    chamado_id = context.user_data.get('id_chamado')
    await atualizar_solucao_chamado(chamado_id, nova_solucao, context.application)
    await update.message.reply_text(f"✅ Solução registrada e usuário notificado para o chamado {chamado_id}.")
    context.user_data.clear()
    return ConversationHandler.END

# Handler genérico para ignorar mensagens fora de contexto
async def ignorar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return

# Registrar comandos no menu
async def definir_comandos(app):
    comandos = [
        BotCommand("start", "Inicia o bot"),
        BotCommand("chamado", "Registrar novo chamado"),
        BotCommand("solucao", "Resolver um chamado (admin)"),
        BotCommand("cancelar", "Cancelar operação")
    ]
    await app.bot.set_my_commands(comandos)

# Main
if __name__ == '__main__':
    init_db()

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).post_init(definir_comandos).build()

    chamado_handler = ConversationHandler(
        entry_points=[CommandHandler("chamado", iniciar_chamado)],
        states={
            SETOR: [CallbackQueryHandler(receber_setor)],
            ALA: [CallbackQueryHandler(receber_ala)],
            LOCALIDADE: [CallbackQueryHandler(receber_localidade)],
            PATRIMONIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_patrimonio)],
            TIPO: [CallbackQueryHandler(receber_tipo)],
            DESCRICAO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_descricao)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar)],
        per_message=False,
    )

    solucao_handler = ConversationHandler(
        entry_points=[CommandHandler("solucao", iniciar_solucao)],
        states={
            SOL_SENHA: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_senha)],
            SOL_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_id_chamado)],
            SOL_TEXTO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_solucao)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar)],
        per_message=False,
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(chamado_handler)
    app.add_handler(solucao_handler)
    app.add_handler(CommandHandler("cancelar", cancelar))
    app.add_handler(MessageHandler(filters.ALL, ignorar), group=1)

    print("🤖 Bot de chamados rodando... Use /chamado")
    app.run_polling()
