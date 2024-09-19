import mysql.connector
import discord
from discord.ext import commands, tasks
from datetime import datetime
from time import sleep
from fpdf import FPDF
import os


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Configurações da conexão com o banco de dados
host = ""
database = ""
username = ""
password = ""
tonyid = 326094154625056768
oitentaid = 1156045534289743912
kelid = 906648805506678825
msgidKEL_TRINTACINCO = 1238318593259601933
msgidTON_QUARENTACINCO = 1222344005509976194
msgidTON_TRINTA = 1222344172300927006
msgidOIT_QUARENTACINCO = 1222378921371242556
logchannel = 1222739787199545385
contador_execucoes = 0
total_lucro_mensal_ultima_c = None
total_custo_produto_mensal_ultima_c = None
total_venda_mensal_ultima_c = None
contador_commits = 0
total_nao_lucro_ultima_c = None
total_lucro_ultima_c = None
total_vendas_ultima_c = None

@bot.event
async def on_ready():
    hrat = datetime.now()
    verifica.start()
    await bot.change_presence(activity=discord.Game(name="HvH cria não cai server"))
    print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] Bot iniciado com sucesso!')

@tasks.loop(minutes=1)  # Executa a cada 30 segundos
async def verifica():
    global contador_execucoes
    global total_lucro_mensal_ultima_c
    global total_custo_produto_mensal_ultima_c
    global total_venda_mensal_ultima_c
    global contador_commits
    global total_nao_lucro_ultima_c
    global total_lucro_ultima_c
    global total_vendas_ultima_c
    try:
        hrat = datetime.now()
        mes_atual = datetime.now().strftime("%Y_mes_%m")
        mes_atual2 = datetime.now().strftime("%Y-%m")
        # Conecta ao banco de dados
        # conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
        # cursor = conexao.cursor()

        # Verifica se a tabela já existe
        # cursor.execute(f"SHOW TABLES LIKE '{mes_atual}'")
        # tabela_existe = cursor.fetchone()

        # if not tabela_existe:
            # Cria a tabela com as colunas especificadas
            # query = f"""
            #            CREATE TABLE {mes_atual} (
            #                lucro_mes VARCHAR(255),
            #                nao_lucro_recebido_mes VARCHAR(255),
            #                vendas_mes VARCHAR(255),
            #                entradas_dc VARCHAR(255),
            #                saidas_dc VARCHAR(255),
            #                inicio_mes_mem VARCHAR(255),
            #                fim_mes_mem VARCHAR(255)
            #            )
            #        """
            # cursor.execute(query)
            # print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] Nova tabela criada {mes_atual}.')

        # cursor.execute(f"SELECT SUM(lucro), SUM(custo_produto) FROM contabilidade WHERE data LIKE '{mes_atual2}%%';")
        # resultado_mensal = cursor.fetchone()
        # total_lucro_mensal, total_custo_produto_mensal = resultado_mensal
        # cursor.execute(f"SELECT COUNT(*) FROM contabilidade WHERE data LIKE '{mes_atual2}%%'")
        # total_venda_mensal = cursor.fetchone()[0]

        # if total_lucro_mensal_ultima_c != total_lucro_mensal and total_venda_mensal_ultima_c != total_venda_mensal and total_custo_produto_mensal_ultima_c != total_custo_produto_mensal:
        # query = (f"UPDATE {mes_atual} SET lucro_mes = {total_lucro_mensal}, nao_lucro_recebido_mes = {total_custo_produto_mensal}, vendas_mes = {total_venda_mensal}")
        # cursor.execute(query)
        # conexao.commit()


        # GUARDAR DADOS DA ULTIMA CONSULTA
        # total_lucro_mensal_ultima_c = total_lucro_mensal
        # total_custo_produto_mensal_ultima_c = total_custo_produto_mensal
        # total_venda_mensal_ultima_c = total_venda_mensal



        # cursor.execute("SELECT SUM(custo_produto), SUM(lucro) FROM contabilidade")
        # resultado = cursor.fetchone()
        # total_nao_lucro, total_lucro = resultado

        # cursor.execute("SELECT COUNT(*) FROM contabilidade")
        # total_vendas = cursor.fetchone()[0]

        # if total_nao_lucro_ultima_c != total_nao_lucro and total_lucro_ultima_c != total_lucro and total_vendas_ultima_c != total_vendas:
        # cursor.execute(f"UPDATE dados_gerais SET lucro_total = {total_lucro}, nao_lucro_recebido = {total_nao_lucro}, vendas_total = {total_vendas}")
        # conexao.commit()

        # total_nao_lucro_ultima_c = total_nao_lucro
        # total_lucro_ultima_c = total_lucro
        # total_vendas_ultima_c = total_vendas

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # cursor.close()
        # conexao.close()
        contador_execucoes += 1
        if contador_execucoes >= 60:
            contador_execucoes = 0  # Reseta o contador após 60 execuções
            print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] 1 hora se passou e {contador_commits} Commits foram executados.')
            contador_commits = 0



@verifica.before_loop
async def antes_do_loop():
    await bot.wait_until_ready()



# @bot.event
# async def on_message(message):
#  # Verifica se a mensagem é um DM.
# if isinstance(message.channel, discord.DMChannel):
#    # Verifica se o autor tem o ID específico.
#   if message.author.id == 326094154625056768:
# Verifica se a mensagem é o comando desejado.
# if message.content == '!oipv':
#     await message.channel.send('ola pv')  # Responde ao usuário.

@bot.command()
async def addcs(ctx, nome, custo, valor_vendido, cliente):
    hrat = datetime.now()
    data_ven = hrat.strftime("%Y-%m-%d")  # Correção no formato da data
    print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] Dados inseridos na tabela contabilidade.')
    # Verifica se o servidor e o usuário têm os IDs corretos
    if ctx.author.id == tonyid:
        lucro = float(valor_vendido) - float(custo)

        # Conecta ao banco de dados
        # conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
        # cursor = conexao.cursor()

        # Use placeholders na query SQL
        # query = "INSERT INTO contabilidade (nome, custo_produto, valor_vendido, data, cliente, lucro) VALUES (%s, %s, %s, %s, %s, %s)"
        # values = (nome, custo, valor_vendido, data_ven, cliente, lucro)
        # cursor.execute(query, values)

        # Confirma a transação
        # conexao.commit()
        # cursor.close()
        # conexao.close()

        await ctx.send('Dados inseridos com sucesso!')
    else:
        await ctx.send('Você não tem permissão para usar este comando.')



@bot.command()
async def cheprice(ctx: commands.Context):
    hrat = datetime.now()
    await ctx.reply("Visite nosso site para verificar os valores do Ch$ats: https://www.80store.site/cheats")
    author = ctx.author.name
    print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] {author} Executou o comando !cheprice.')

@bot.command()
async def nicktuto(ctx: commands.Context):
    hrat = datetime.now()
    await ctx.reply("Como alterar o nick das contas SDA: https://www.youtube.com/watch?v=r44Jz1QGlW0")
    author = ctx.author.name
    print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] {author} Executou o comando !nicktuto.')

@bot.command()
async def consulacc(ctx: commands.Context, login):
    hrat = datetime.now()
    id_do_autor = ctx.author.id
    author_name = ctx.author.name
    # Conecta ao banco de dados
    # conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    # cursor = conexao.cursor()
    if id_do_autor == tonyid or id_do_autor == oitentaid or id_do_autor == kelid:
        if id_do_autor == tonyid:
            n_stock = "tony_stock45"
            n_pasta = "tony"
        elif id_do_autor == oitentaid:
            n_stock = "80s_stock45"
            n_pasta = "80s"
        # cursor.execute(
        #     f"SELECT id, login, senha, email, email_password, vendida FROM {n_stock} WHERE login = '{login}';")
        # valores = cursor.fetchall()
        # file_path = f'{n_pasta}_mafiles/{valores[0][1]}.maFile'
        # if valores[0][5] == "0":
        #     status = "NÃO"
        # elif valores[0][5] == "1":
        #     status = "SIM"

        # await ctx.reply(f"""
        # ||[DEBUG INFOS - ID: {valores[0][0]} STATS = {valores[0][5]} SNAME = {n_stock}]||

        # Ola Segue as informações da conta consultada:

        # NOME: {valores[0][1]}
        # SENHA: {valores[0][2]}
        # EMAIL: {valores[0][3]}
        # EMAIL SENHA: {valores[0][4]}
        # ENVIADA = {status}

        # Segue o maFile:
        # """)
        # try:
        #     with open(file_path, 'rb') as file:
        #         # Especifica um nome diferente para o arquivo ao enviá-lo
        #         await ctx.send(file=discord.File(file, f'{valores[0][1]}.maFile'))
        # except FileNotFoundError:
        #     await ctx.send('Arquivo não encontrado.')
    else:
        await ctx.reply("Voce nao tem perm")
    print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] {author_name} Executou o comando !consulacc {login}.')

@bot.command()
async def enviar(ctx):
    file_path = 'tony_mafiles/.maFile'
    try:
        with open(file_path, 'rb') as file:
            # Especifica um nome diferente para o arquivo ao enviá-lo
            await ctx.send(file=discord.File(file, '.maFile'))
    except FileNotFoundError:
        await ctx.send('Arquivo não encontrado.')


@bot.command()
async def revec(ctx: commands.Context, login):
    hrat = datetime.now()
    author_name = ctx.author.name
    canallog = bot.get_channel(logchannel)
    id_do_autor = ctx.author.id
    conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    cursor = conexao.cursor()
    if id_do_autor == tonyid:
        n_stock = "tony_stock45"
        cursor.execute(f"SELECT id, login FROM {n_stock} WHERE login = '{login}';")
        valores = cursor.fetchall()
        update_query = f"UPDATE {n_stock} SET vendida = '0' WHERE {n_stock}.id = {valores[0][0]};"
        cursor.execute(update_query)
        conexao.commit()  # Adiciona o commit aqui
        await canallog.send(
            f'Conta com LOGIN {valores[0][1]} (ID: {valores[0][0]}) Foi revertida para NÃO ENVIADA no nosso DATABASE!')
    elif id_do_autor == oitentaid:
        n_stock = "80s_stock45"
        cursor.execute(f"SELECT id, login FROM {n_stock} WHERE login = '{login}';")
        valores = cursor.fetchall()
        update_query = f"UPDATE {n_stock} SET vendida = '0' WHERE {n_stock}.id = {valores[0][0]};"
        cursor.execute(update_query)
        conexao.commit()  # Adiciona o commit aqui
        await canallog.send(
            f'Conta com LOGIN {valores[0][1]} (ID: {valores[0][0]}) Foi revertida para NÃO ENVIADA no nosso DATABASE!')
    elif id_do_autor == kelid:
        n_stock = "kel_stock35"
        cursor.execute(f"SELECT id, login FROM {n_stock} WHERE login = '{login}';")
        valores = cursor.fetchall()
        update_query = f"UPDATE {n_stock} SET vendida = '0' WHERE {n_stock}.id = {valores[0][0]};"
        cursor.execute(update_query)
        conexao.commit()  # Adiciona o commit aqui
        await canallog.send(
            f'Conta com LOGIN {valores[0][1]} (ID: {valores[0][0]}) Foi revertida para NÃO ENVIADA no nosso DATABASE!')
    cursor.close()
    conexao.close()

    channel = bot.get_channel(1222046050039107694)
    # Busca a mensagem pelo ID
    msgTON_QUARENTACINCO = await channel.fetch_message(msgidTON_QUARENTACINCO)
    msgOIT_QUARENTACINCO = await channel.fetch_message(msgidOIT_QUARENTACINCO)
    msgKEL_TRINTACINCO = await channel.fetch_message(msgidKEL_TRINTACINCO)
    id_do_autor = ctx.author.id
    conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM tony_stock45 WHERE vendida = 0")
    TON_stockquant_QUARENTACINCO = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM kel_stock35 WHERE vendida = 0")
    KEL_stockquant_TRINTACINCO = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM 80s_stock45 WHERE vendida = 0")
    OIT_stockquant_QUARENTACINCO = cursor.fetchall()
    cursor.close()
    conexao.close()
    nome_do_autor = ctx.author.display_name
    avatar = ctx.author.avatar
    if id_do_autor == tonyid or id_do_autor == oitentaid or id_do_autor == kelid:
        # Pega o embed existente da mensagem
        embedTON_QUARENTACINCO = msgTON_QUARENTACINCO.embeds[0]
        embedOIT_QUARENTACINCO = msgOIT_QUARENTACINCO.embeds[0]
        embedKEL_TRINTACINCO = msgKEL_TRINTACINCO.embeds[0]
        # Atualiza apenas a descrição do embed
        embedTON_QUARENTACINCO.description = f"Estoque: {TON_stockquant_QUARENTACINCO[0][0]}"
        embedOIT_QUARENTACINCO.description = f"Estoque: {OIT_stockquant_QUARENTACINCO[0][0]}"
        embedKEL_TRINTACINCO.description = f"Estoque: {KEL_stockquant_TRINTACINCO[0][0]}"
        # Edita a mensagem com o embed atualizado
        await msgTON_QUARENTACINCO.edit(embed=embedTON_QUARENTACINCO)
        await msgOIT_QUARENTACINCO.edit(embed=embedOIT_QUARENTACINCO)
        await msgKEL_TRINTACINCO.edit(embed=embedKEL_TRINTACINCO)
    print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] {author_name} Executou o comando !reve {login} e o Estoque foi atualizado.')

@bot.command()
async def sendc(ctx: commands.Context):
    hrat = datetime.now()
    author_name = ctx.author.name
    canallog = bot.get_channel(logchannel)
    id_do_autor = ctx.author.id
    conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    cursor = conexao.cursor()
    if id_do_autor == tonyid:
        n_stock = "tony_stock45"
        cursor.execute(f"SELECT * FROM {n_stock} WHERE vendida = 0 ORDER BY RAND() LIMIT 1;")
        valores = cursor.fetchall()
        if valores:
            update_query = f"UPDATE {n_stock} SET vendida = '1' WHERE {n_stock}.id = {valores[0][0]};"
            cursor.execute(update_query)
            conexao.commit()  # Adiciona o commit aqui
            await canallog.send(
                f'Conta com LOGIN {valores[0][1]} (ID: {valores[0][0]}) está com status de ENVIADA em nosso DATABASE! Para reverter essa situação de o comando !reve {valores[0][1]}')
        else:
            print("Nenhum registro encontrado para atualizar.")

    elif id_do_autor == oitentaid:
        n_stock = "80s_stock45"
        cursor.execute(f"SELECT * FROM {n_stock} WHERE vendida = 0 ORDER BY RAND() LIMIT 1;")
        valores = cursor.fetchall()
        update_query = f"UPDATE {n_stock} SET vendida = '1' WHERE {n_stock}.id = {valores[0][0]};"
        cursor.execute(update_query)
        conexao.commit()  # Adiciona o commit aqui
        await canallog.send(
            f'Conta com LOGIN {valores[0][1]} (ID: {valores[0][0]}) está com status de ENVIADA em nosso DATABASE! Para reverter essa situação de o comando !reve {valores[0][1]}')

    elif id_do_autor == kelid:
        n_stock = "80s_stock45"
        cursor.execute(f"SELECT * FROM {n_stock} WHERE vendida = 0 ORDER BY RAND() LIMIT 1;")
        valores = cursor.fetchall()
        update_query = f"UPDATE {n_stock} SET vendida = '1' WHERE {n_stock}.id = {valores[0][0]};"
        cursor.execute(update_query)
        conexao.commit()  # Adiciona o commit aqui
        await canallog.send(
            f'Conta com LOGIN {valores[0][1]} (ID: {valores[0][0]}) está com status de ENVIADA em nosso DATABASE! Para reverter essa situação de o comando !reve {valores[0][1]}')
    cursor.close()
    conexao.close()
    if id_do_autor == tonyid:
        file_path = f'tony_mafiles/{valores[0][1]}.maFile'
    elif id_do_autor == oitentaid:
        file_path = f'80s_mafiles/{valores[0][1]}.maFile'
    elif id_do_autor == kelid:
        file_path = f'kel_mafiles/{valores[0][1]}.maFile'
    if id_do_autor == tonyid or id_do_autor == oitentaid or id_do_autor == kelid:
        await ctx.reply(f"""
||[DEBUG INFOS - ID: {valores[0][0]} STATS = {valores[0][5]} SNAME = {n_stock}]||

Ola! Segue os dados solicitados:

NOME: {valores[0][1]}
SENHA: {valores[0][2]}
EMAIL: {valores[0][3]}
EMAIL SENHA: {valores[0][4]}

Segue o maFile e o SDA:
    """)
        try:
            with open(file_path, 'rb') as file:
                # Especifica um nome diferente para o arquivo ao enviá-lo
                await ctx.send(file=discord.File(file, f'{valores[0][1]}.maFile'))
            file_path2 = 'SDA - STEAM DESKTOP AUTENTICATOR.zip'
            with open(file_path2, 'rb') as file2:
                await ctx.send(file=discord.File(file2))
        except FileNotFoundError:
            await ctx.send('Arquivo não encontrado.')
        await ctx.send('Segue o tutorial de como usar o SDA: https://youtu.be/92J8lQRA1GU')
    else:
        await ctx.reply("Voce nao tem perm")

        # Obtem o objeto do canal usando o ID do canal
    channel = bot.get_channel(1222046050039107694)
    # Busca a mensagem pelo ID
    msgTON_QUARENTACINCO = await channel.fetch_message(msgidTON_QUARENTACINCO)
    msgOIT_QUARENTACINCO = await channel.fetch_message(msgidOIT_QUARENTACINCO)
    msgKEL_TRINTACINCO = await channel.fetch_message(msgidKEL_TRINTACINCO)
    id_do_autor = ctx.author.id
    conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM tony_stock45 WHERE vendida = 0")
    TON_stockquant_QUARENTACINCO = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM kel_stock35 WHERE vendida = 0")
    KEL_stockquant_TRINTACINCO = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM 80s_stock45 WHERE vendida = 0")
    OIT_stockquant_QUARENTACINCO = cursor.fetchall()
    cursor.close()
    conexao.close()
    nome_do_autor = ctx.author.display_name
    avatar = ctx.author.avatar
    if id_do_autor == tonyid or id_do_autor == oitentaid or id_do_autor == kelid:
        # Pega o embed existente da mensagem
        embedTON_QUARENTACINCO = msgTON_QUARENTACINCO.embeds[0]
        embedOIT_QUARENTACINCO = msgOIT_QUARENTACINCO.embeds[0]
        embedKEL_TRINTACINCO = msgKEL_TRINTACINCO.embeds[0]
        # Atualiza apenas a descrição do embed
        embedTON_QUARENTACINCO.description = f"Estoque: {TON_stockquant_QUARENTACINCO[0][0]}"
        embedOIT_QUARENTACINCO.description = f"Estoque: {OIT_stockquant_QUARENTACINCO[0][0]}"
        embedKEL_TRINTACINCO.description = f"Estoque: {KEL_stockquant_TRINTACINCO[0][0]}"
        # Edita a mensagem com o embed atualizado
        await msgTON_QUARENTACINCO.edit(embed=embedTON_QUARENTACINCO)
        await msgOIT_QUARENTACINCO.edit(embed=embedOIT_QUARENTACINCO)
        await msgKEL_TRINTACINCO.edit(embed=embedKEL_TRINTACINCO)
    print(f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO] {author_name} Executou o comando !sell45 e o Estoque foi atualizado a conta de ID:{valores[0][0]} foi vendida.')

@bot.command()
async def upestoquec(ctx: commands.Context):
    # Obtem o objeto do canal usando o ID do canal
    channel = bot.get_channel(1222046050039107694)
    # Busca a mensagem pelo ID
    msgTON_QUARENTACINCO = await channel.fetch_message(msgidTON_QUARENTACINCO)
    msgOIT_QUARENTACINCO = await channel.fetch_message(msgidOIT_QUARENTACINCO)
    msgKEL_TRINTACINCO = await channel.fetch_message(msgidKEL_TRINTACINCO)
    id_do_autor = ctx.author.id
    conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM tony_stock45 WHERE vendida = 0")
    TON_stockquant_QUARENTACINCO = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM kel_stock35 WHERE vendida = 0")
    KEL_stockquant_TRINTACINCO = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM 80s_stock45 WHERE vendida = 0")
    OIT_stockquant_QUARENTACINCO = cursor.fetchall()
    cursor.close()
    conexao.close()
    nome_do_autor = ctx.author.display_name
    avatar = ctx.author.avatar
    if id_do_autor == tonyid or id_do_autor == oitentaid:
        # Pega o embed existente da mensagem
        embedTON_QUARENTACINCO = msgTON_QUARENTACINCO.embeds[0]
        embedOIT_QUARENTACINCO = msgOIT_QUARENTACINCO.embeds[0]
        embedKEL_TRINTACINCO = msgKEL_TRINTACINCO.embeds[0]
        # Atualiza apenas a descrição do embed
        embedTON_QUARENTACINCO.description = f"Estoque: {TON_stockquant_QUARENTACINCO[0][0]}"
        embedOIT_QUARENTACINCO.description = f"Estoque: {OIT_stockquant_QUARENTACINCO[0][0]}"
        embedKEL_TRINTACINCO.description = f"Estoque: {KEL_stockquant_TRINTACINCO[0][0]}"
        # Edita a mensagem com o embed atualizado
        await msgTON_QUARENTACINCO.edit(embed=embedTON_QUARENTACINCO)
        await msgOIT_QUARENTACINCO.edit(embed=embedOIT_QUARENTACINCO)
        await msgKEL_TRINTACINCO.edit(embed=embedKEL_TRINTACINCO)

    await ctx.message.delete()


@bot.command()
async def enviar_embedc(ctx: commands.Context):
    #    ID do canal específico
    canal = bot.get_channel(1222046050039107694)
    avatar = ctx.author.avatar

    hrat = datetime.now()  # Substitua ID_DO_CANAL pelo ID do canal desejado
    embed = discord.Embed(
        title=(f'ESTOQUE PRIME-STATUS Kel'),
        description=f"""Estoque: N/A""",



        color=discord.Color.blue()  # Você pode escolher a cor que preferir
    )

    # Enviar o embed para o canal específico
    await canal.send(embed=embed)

@bot.command()
async def upcontc(ctx: commands.Context):
    conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    cursor = conexao.cursor()
    cursor.execute("SELECT lucro_mes, nao_lucro_recebido_mes, vendas_mes FROM 2024_mes_04")
    results = cursor.fetchall()
    cursor = conexao.cursor()
    cursor.execute("SELECT lucro_mes, nao_lucro_recebido_mes, vendas_mes FROM 2024_mes_04")
    results = cursor.fetchall()
    cursor.execute("SELECT lucro_total, nao_lucro_recebido, vendas_total FROM dados_gerais")
    results2 = cursor.fetchall()
    cursor.close()
    conexao.close()

    # Obtenha o canal de texto pelo ID
    channel = bot.get_channel(1228027708517388459)

    # Obtenha a mensagem pelo ID
    embed_id = 1230859850058305627
    msgembed = await channel.fetch_message(embed_id)

    # Atualize a descrição do embed
    embed_o = msgembed.embeds[0]
    embed_o.description = f"""
    Lucro total: {results2[0][0]}
    Total de vendas: {results2[0][2]}
    Lucro no mês: {results[0][0]}
    Total de vendas no mês: {results[0][2]}

    Total não lucro recebido: {results2[0][1]}
    Total não lucro recebido no mês: {results[0][1]}
    """

    # Edite a mensagem com o embed atualizado
    await msgembed.edit(embed=embed_o)


@bot.command()
async def editc(ctx):
# Supondo que você tenha o ID da mensagem e do canal armazenados
    channel = bot.get_channel(1222046050039107694)
    message = await channel.fetch_message(1238314431176249364)
    embed = message.embeds[0]  # Pega o primeiro embed da mensagem
    embed.title = 'ESTOQUE PRIME-STATUS Kel'  # Altera o título do embed
    await message.edit(embed=embed)  # Edita a mensagem com o novo embed

class PDF(FPDF):
    def header(self):
        # Logo (centralized)
        # self.image('logo.png', x=10, y=8, w=33)
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, '80 SOLUTIONS SISTEMA DE GESTÃO INTEGRADA', 0, 1, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

# Comando para gerar o relatório
@bot.command()
async def relatc(ctx):
    # Conecte ao banco de dados
    conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, custo_produto, valor_vendido, data, cliente FROM contabilidade")
    results = cursor.fetchall()
    cursor.close()
    conexao.close()

    # Crie o PDF
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)

    # Adicione um cabeçalho de tabela
    pdf.cell(0, 10, 'ID Nome Custo Produto Valor Vendido Data Cliente', 0, 1, 'C')

    # Adicione os dados do banco de dados ao PDF
    pdf.set_font('Arial', '', 10)
    for row in results:
        id, nome, custo_produto, valor_vendido, data, cliente = row
        line = f'ID: {id}, Nome: {nome}, Custo: {custo_produto}, Valor: {valor_vendido}, Data: {data}, Cliente: {cliente}'
        pdf.multi_cell(0, 10, line, 0, 1)

    # Salve o PDF
    pdf_file_name = 'relatorio.pdf'
    pdf.output(pdf_file_name)

    # Envie o PDF no Discord
    with open(pdf_file_name, 'rb') as pdf_file:
        await ctx.send(file=discord.File(pdf_file, pdf_file_name))

    # Apague o PDF do diretório
    os.remove(pdf_file_name)



@bot.event
async def on_member_join(member):
    channelcont = bot.get_channel(930969491708477541)
    membertot = channelcont.guild.member_count
    hrat = datetime.now()
    mes_tab = datetime.now().strftime("%Y_mes_%m")
    mes_info = datetime.now().strftime("%d")

    channellog = bot.get_channel(883039291570262016)  # Substitua ID_DO_CANAL pelo ID do canal desejado
    embed = discord.Embed(
        title=(f'ENTRADA - [{hrat.strftime("%d/%m/%Y %H:%M:%S")}]'),
        description=(f"{member.mention} Entrou no servidor!"),
        color=discord.Color.green()  # Você pode escolher a cor que preferir
    )
    embed.set_thumbnail(url=member.display_avatar.url)  # Define o avatar do membro como thumbnail do embed
    await channellog.send(embed=embed)

    # Conecta ao banco de dados
    # conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    # cursor = conexao.cursor()
    # if mes_info == "01":
    #     query = (f"UPDATE {mes_tab} SET inicio_mes_mem = {membertot}")
    #     cursor.execute(query)
    #     conexao.commit()
    # elif mes_info == "29":
    #     query = (f"UPDATE {mes_tab} SET fim_mes_mem = {membertot}")
    #     cursor.execute(query)
    #     conexao.commit()

    # query = (f"UPDATE {mes_tab} SET entradas_dc = entradas_dc + 1")
    # cursor.execute(query)
    # conexao.commit()
    # cursor.close()
    # conexao.close()

    ag1 = ""
    ag2 = ""
    ag3 = ""
    ag4 = ""
    # Substitua 'ID_DO_CANAL' pelo ID do canal onde você deseja atualizar o tópico
    numero = str(membertot)  # Substitua pela string do número desejado
    if membertot < 1000:
        ag1 = "<:ZERO:1222021893419434085>"
    for indice, algarismo in enumerate(numero):
        if ag1 == "<:ZERO:1222021893419434085>":
            if indice == 1:
                if algarismo == "0":
                    ag2 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag2 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag2 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag2 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag2 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag2 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag2 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag2 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag2 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag2 = "<:NOVE:1222022023631474689>"
            elif indice == 2:
                if algarismo == "0":
                    ag3 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag3 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag3 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag3 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag3 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag3 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag3 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag3 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag3 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag3 = "<:NOVE:1222022023631474689>"
            elif indice == 3:
                if algarismo == "0":
                    ag4 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag4 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag4 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag4 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag4 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag4 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag4 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag4 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag4 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag4 = "<:NOVE:1222022023631474689>"
        else:
            if indice == 0:
                if algarismo == "0":
                    ag1 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag1 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag1 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag1 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag1 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag1 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag1 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag1 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag1 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag1 = "<:NOVE:1222022023631474689>"
            elif indice == 1:
                if algarismo == "0":
                    ag2 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag2 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag2 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag2 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag2 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag2 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag2 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag2 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag2 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag2 = "<:NOVE:1222022023631474689>"
            elif indice == 2:
                if algarismo == "0":
                    ag3 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag3 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag3 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag3 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag3 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag3 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag3 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag3 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag3 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag3 = "<:NOVE:1222022023631474689>"
            elif indice == 3:
                if algarismo == "0":
                    ag4 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag4 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag4 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag4 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag4 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag4 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag4 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag4 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag4 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag4 = "<:NOVE:1222022023631474689>"
    if membertot < 1000:
        await channelcont.edit(topic=f'Total de Membros: {ag1}{ag2}{ag3}{ag4}')
    else:
        await channelcont.edit(topic=f'Total de Membros:  ({ag1}{ag2}{ag3}{ag4})')
    print(
        f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO    ] Tópico do canal {channelcont.name} atualizado com sucesso!')


@bot.event
async def on_member_remove(member):
    hrat = datetime.now()
    channellog = bot.get_channel(883039291570262016)  # Substitua ID_DO_CANAL pelo ID do canal desejado
    channelcont = bot.get_channel(930969491708477541)
    membertot = channelcont.guild.member_count
    mes_tab = datetime.now().strftime("%Y_mes_%m")
    mes_info = datetime.now().strftime("%d")

    embed = discord.Embed(
        title=(f'SAIDA - [{hrat.strftime("%d/%m/%Y %H:%M:%S")}]'),
        description=f"{member.mention} Saiu do servidor!",
        color=discord.Color.red()  # Você pode escolher a cor que preferir
    )
    embed.set_thumbnail(url=member.display_avatar.url)  # Define o avatar do membro como thumbnail do embed
    await channellog.send(embed=embed)

    # Conecta ao banco de dados
    # conexao = mysql.connector.connect(host=host, user=username, password=password, database=database)
    # cursor = conexao.cursor()
    # if mes_info == "01":
    #     query = (f"UPDATE {mes_tab} SET inicio_mes_mem = {membertot}")
    #     cursor.execute(query)
    #     conexao.commit()
    # elif mes_info == "29":
    #     query = (f"UPDATE {mes_tab} SET fim_mes_mem = {membertot}")
    #     cursor.execute(query)
    #     conexao.commit()

    # query = (f"UPDATE {mes_tab} SET saidas_dc = saidas_dc + 1")
    # cursor.execute(query)
    # conexao.commit()
    # cursor.close()
    # conexao.close()

    ag1 = ""
    ag2 = ""
    ag3 = ""
    ag4 = ""
    # Substitua 'ID_DO_CANAL' pelo ID do canal onde você deseja atualizar o tópico
    numero = str(membertot)  # Substitua pela string do número desejado
    if membertot < 1000:
        ag1 = "<:ZERO:1222021893419434085>"
    for indice, algarismo in enumerate(numero):
        if ag1 == "<:ZERO:1222021893419434085>":
            if indice == 1:
                if algarismo == "0":
                    ag2 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag2 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag2 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag2 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag2 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag2 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag2 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag2 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag2 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag2 = "<:NOVE:1222022023631474689>"
            elif indice == 2:
                if algarismo == "0":
                    ag3 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag3 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag3 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag3 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag3 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag3 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag3 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag3 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag3 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag3 = "<:NOVE:1222022023631474689>"
            elif indice == 3:
                if algarismo == "0":
                    ag4 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag4 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag4 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag4 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag4 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag4 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag4 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag4 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag4 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag4 = "<:NOVE:1222022023631474689>"
        else:
            if indice == 0:
                if algarismo == "0":
                    ag1 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag1 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag1 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag1 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag1 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag1 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag1 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag1 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag1 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag1 = "<:NOVE:1222022023631474689>"
            elif indice == 1:
                if algarismo == "0":
                    ag2 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag2 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag2 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag2 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag2 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag2 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag2 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag2 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag2 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag2 = "<:NOVE:1222022023631474689>"
            elif indice == 2:
                if algarismo == "0":
                    ag3 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag3 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag3 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag3 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag3 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag3 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag3 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag3 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag3 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag3 = "<:NOVE:1222022023631474689>"
            elif indice == 3:
                if algarismo == "0":
                    ag4 = "<:ZERO:1222021893419434085>"
                elif algarismo == "1":
                    ag4 = "<:UM:1222021905067020309>"
                elif algarismo == "2":
                    ag4 = "<:DOIS:1222021915820949554>"
                elif algarismo == "3":
                    ag4 = "<:TRES:1222021926957092924>"
                elif algarismo == "4":
                    ag4 = "<:QUATRO:1222021952177307648>"
                elif algarismo == "5":
                    ag4 = "<:CINCO:1222021962151231569>"
                elif algarismo == "6":
                    ag4 = "<:SEIS:1222021971957649442>"
                elif algarismo == "7":
                    ag4 = "<:SETE:1222022001405722747>"
                elif algarismo == "8":
                    ag4 = "<:OITO:1222022011702743113>"
                elif algarismo == "9":
                    ag4 = "<:NOVE:1222022023631474689>"
    if membertot < 1000:
        await channelcont.edit(topic=f'Total de Membros: {ag1}{ag2}{ag3}{ag4}')
    else:
        await channelcont.edit(topic=f'Total de Membros:  ({ag1}{ag2}{ag3}{ag4})')
    print(
        f'[{hrat.strftime("%d-%m-%Y %H:%M:%S")}] [INFO    ] Tópico do canal {channelcont.name} atualizado com sucesso!')



bot.run("")