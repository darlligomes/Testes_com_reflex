import reflex as rx

class State(rx.State):
    """The app state."""
    ...

class TextoApresentacao(rx.State):
    titulo: str = "Olá, eu sou Darllington Gomes!"
    subtitulo: str = "Assistente de Sistemas na área indústrial, graduando em Análise e Desenvolvimento de Sistemas."
    resumo: str = """ 
    💻 Apaixonado por Tecnologia, Inovação e Desenvolvimento de Soluções
Sou técnico em Informática e estudante de Análise e Desenvolvimento de Sistemas, conclusão prevista para 2026), com experiência no uso de ERP para suporte ao usuário, seja cliente ou usuário do próprio sistema. Durante minha jornada, tive a oportunidade de aplicar e expandir o meu conhecimento na área de dados, utilizando o MySql com ferramentas como o Toad for Oracle, com o objetivo de, por meio de Querys que resultam em relatórios, proporcionar análises sobre resultados. 
    \n
    🔧 Experiência Profissional
Atualmente, como Assistente de Sistemas, atuo no suporte a sistemas corporativos, ajustando queries, analisando requisitos de relatórios e solucionando situações na indústria em que atuo. Também tenho experiência com suporte remoto na área de redes, a qual junto ao time que fiz parte consegui promover atendimento de qualidade e resoluções de problemas relacionados a conexão.
    \n
    📚 Formação e Aprendizado Contínuo
Sou adepto ao aprendizado contínuo e expansivo, onde contínuo e complemento minha formação com diversos cursos livres, o que vai da análise de dados (Iniciando com o MySql e partindo para a linguagem Python, que também serve para Django e automações com Selenium, e Power B.I., ferramenta impecável para relatórios de negócios.) até Gestão Financeira e Logística, onde reforço a minha visão que a T.I. deve buscar adentrar em outras áreas para implementar ainda mais a tecnologia e promover melhores resultados.
    \n
    
📌 Objetivo Profissional
Busco, por meio da T.I., promover uma contribuição que valorize a inovação e o desenvolvimento de novas soluções. Meu foco está em projetos que desafiem meu potencial, ao mesmo tempo que promova uma integração de conhecimentos de diferentes áreas e que gere um impacto positivo na produtividade e em resultados.
    """
    
    
def botao(nome: str, cor: str, cor_de_fundo: str, site: str, icone: rx.Component) -> rx.Component:
        return rx.link(
        rx.button(icone, nome, style={"color": cor, "background_color": cor_de_fundo, 
                                      "cursor": "pointer",}
                  ),
        href=site,
        is_external=True,   
    )



    
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading(TextoApresentacao.titulo, size="9"),
            rx.color_mode.button(position="top-right", style={"margin-bottom": "40px"}),

            rx.text(TextoApresentacao.subtitulo, size="5"),
            rx.hstack(
                botao(
                    "Linkedin", 
                    rx.color_mode_cond(dark="white", light="black"), 
                    "#3E63DD", 
                    "https://www.linkedin.com/in/darllingtongomes/", 
                    rx.icon(tag="linkedin", size=24)
                ),
                botao(
                    "GitHub", 
                    rx.color_mode_cond(dark="black", light="white"), 
                    rx.color_mode_cond(dark="white", light="black"), 
                    "https://github.com/darlligomes", 
                    rx.icon(tag="github", size=24)
                ),
                botao(
                    "Instagram", 
                    "white",
                    "#500F1C", 
                    "https://www.instagram.com/darlligomes/", 
                    rx.icon(tag="instagram", size=24)
                ),
                spacing="6",
                justify= "center",
                width="100%",
            ),
          rx.card(
                rx.vstack(
                    rx.foreach(
                        TextoApresentacao.resumo.split("\n"),  # Usando rx.foreach
                        lambda line, idx: rx.text(
                            line, 
                            size="3", 
                            style=rx.cond(
                                idx == 0,  # Se for a primeira linha (índice 0)
                                {"font_weight": "bold"},  # Aplica negrito na primeira linha
                                {}  # Para as outras, sem estilo
                            )
                        )
                    ),
                    spacing="3"
                )
                ),
            spacing="5",
            min_height="100vh",
            padding_top="5vh",
        ),

    )
    
app = rx.App(    
    theme=rx.theme(
        appearance="light", has_background=True, radius="small", accent_color="indigo"
    ),
        stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
    ],)


app.style = {
    "transition": "all 0.3s ease",
}

app.add_page(index, title = "Darllington Gomes")