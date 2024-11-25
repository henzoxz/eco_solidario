import streamlit as st

def main():
    if "pagina" not in st.session_state:
        st.session_state.pagina = "home"

    if "usuario" not in st.session_state:
        st.session_state.usuario = {"nome": "", "email": "", "senha": ""}

    st.sidebar.image("https://i.imgur.com/JwwPz4t.png")
    escolha = st.sidebar.selectbox("ESCOLHA O QUE DESEJAR", ["SUA CONTA", "CADASTRO", "LOGIN", "SOBRE", "CHAVE PARA DOAÇÕES", "FEEDBACK"])

    if escolha == "SOBRE":
        st.header("Sobre Nós")
        st.write(""" 
        Eco Solidário ONG fundada por Henry, Hugo, Henzo, Guilherme e Bruno, com a missão de apoiar pessoas em situação de vulnerabilidade, incluindo moradores de rua e refugiados. Nosso objetivo é arrecadar fundos e itens essenciais como alimentos, roupas, cobertores, produtos de higiene e materiais de primeira necessidade, para proporcionar dignidade e suporte às pessoas que mais necessitam. 
        Através de campanhas de arrecadação e parcerias com empresas e voluntários, buscamos aliviar o sofrimento imediato e oferecer um acolhimento humanitário. 
        Além disso, a Eco Solidário promove a inclusão social e a conscientização sobre as questões enfrentadas por essas populações, integrando ações de solidariedade com práticas sustentáveis e o compromisso com os direitos humanos, criando um impacto positivo tanto nas vidas das pessoas atendidas quanto na sociedade como um todo
        """)

    elif escolha == "CHAVE PARA DOAÇÕES":
        st.header("Chave para Doações")
        st.write(""" 
            A chave para doações é um código exclusivo que permite fazer contribuições financeiras para nossas iniciativas ambientais e de ajuda social.  
            *Chave para doação:* *ABC123XYZ*
            Este código pode ser utilizado em nossa plataforma de pagamento online para enviar sua doação e apoiar nossa causa.
        """)

    elif escolha == "FEEDBACK":
        st.header("Feedback")
        feedback = st.text_area("Deixe aqui seu feedback:")
        if st.button("Enviar"):
            st.success("Feedback enviado! Obrigado por compartilhar sua opinião.")

    elif escolha == "LOGIN":
        st.header("Login")
        nome = st.text_input("Digite seu nome de Usuário")
        email = st.text_input("Digite seu e-mail")
        senha = st.text_input("Digite sua senha", type="password")
        if st.button("Clique"):
            st.session_state.usuario["nome"] = nome
            st.session_state.usuario["email"] = email
            st.session_state.usuario["senha"] = senha
            st.session_state.pagina = "conta"
            st.success("LOGIN REALIZADO COM SUCESSO! BEM VINDO A ECO SOLIDÁRIO!")



    elif escolha == "CADASTRO":
        st.header("Cadastre-se")
        nome = st.text_input("Digite seu nome de Usuário")
        email = st.text_input("Digite seu e-mail")
        senha = st.text_input("Digite sua senha", type="password")
        senhanovamente = st.text_input("Digite sua senha novamente", type="password")
        
        if st.button("Clique"):
            st.session_state.usuario["nome"] = nome
            st.session_state.usuario["email"] = email
            st.session_state.usuario["senha"] = senha
            st.session_state.pagina = "conta"
            st.success("CADASTRO REALIZADO COM SUCESSO! BEM VINDO A ECO SOLIDÁRIO!")

    elif escolha == "SUA CONTA":
        st.image("https://i.imgur.com/pZ0EHaf.jpeg")
        if st.session_state.pagina == "home":
            st.title("Você ainda não possui conta! Cadastre-se indo até a pagina localizada na selectbox à esquerda.")

        elif st.session_state.pagina == "conta":
            st.header("Sua Conta")
            st.write(f"Nome: {st.session_state.usuario['nome']}")
            st.write(f"E-mail: {st.session_state.usuario['email']}")
            st.write(f"Senha: {st.session_state.usuario['senha']}")
            

main()
