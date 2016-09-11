#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

# Configurações Base
SITENAME = u'Python Norte'
AUTHOR = u'PyNorte'
THEME = "themes/malt"
MALT_BASE_COLOR = "blue-grey"


META_DESCRIPTION = '''O PyNorte é um grupo de usuários (profissionais e
                      amadores) da linguagem Python, onde prezamos pela troca de
                      conhecimento, respeito mútuo e diversidade (tanto de opinião
                      quanto de tecnologias).'''

META_KEYWORDS = ['pynorte', 'python', 'amazonas', 'desenvolvimento',
                 'acre', 'para', 'tocantins', 'rondonia', 'roraima', 'amapa']

# Referências à Github
GITHUB_REPO = "https://github.com/PyNorte/grupybr-pynorte"
GITHUB_BRANCH = "master"

# Imagens
ARTICLE_BANNERS_FOLDER = "images/banners"
SITE_LOGO = "images/logo.png"
SITE_LOGO_MOBILE = "images/logo-mobile.png"

# Home settings
WELCOME_TITLE = "Seja bem vindo ao {}".format(SITENAME)
WELCOME_TEXT = "Grupo de usuários da linguagem Python do Norte do Brasil."
SITE_BACKGROUND_IMAGE = "images/banners/background.png"
FOOTER_ABOUT = "O Grupo Python Norte é uma comunidade de usuários do Acre, Amapá, Amazonas, Pará, Rondônia, Roraima e Tocantins"

# Tema do Syntax Hightlight
PYGMENTS_STYLE = "perldoc"

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    # {
    #      "title": "Comunidade",
    #      "href": "comunidade",
    # },
    {
        "title": "Membros",
        "href": "membros",
    },
#    {
#        "title": "Blog",
#        "href": "blog",
#    },
]

# Navbar Links do Blog
NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        "href": "bit.ly/pynorte",
        "icon": "fa-paper-plane",
        "text": "Telegram",
    },
    {
        "href": "http://facebook.com/pynorte",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
    {
        "href": "https://groups.google.com/d/forum/pynorte",
        "icon": "fa-envelope",
        "text": "Lista de e-mail",
    },
    {
        "href": "https://github.com/PyNorte",
        "icon": "fa-github",
        "text": "PyNorte no GitHub",
    },
    {
        "href": "https://github.com/grupydf",
        "icon": "fa-github",
        "text": "Grupy-DF",
    },
    {
        "href": "http://wiki.python.org.br/",
        "icon": "fa-globe",
        "text": "Python Brasil",
    },
    {
        "href": "https://python.org",
        "icon": "fa-globe",
        "text": "Python",
    },
    {
        "href": "http://www.pythonclub.com.br/",
        "icon": "fa-globe",
        "text": "PythonClub",
    },
    {
        "href": "http://dojoto.info/",
        "icon": "fa-globe",
        "text": "CodingDojoTocantins"
    },
)

# Membros do Grupy
MEMBROS = OrderedDict((
    ("Nilo Menezes", {
        "twitter": "@lskbr",
        "github": "lskbr",
        "site": {
            "nome": "Nilo Menezes",
            "href": "http://www.nilo.pro.br",
        }
    }),
    ("Adriano Praia", {
        "github": "adrianopraia",
    }),
    ("Fábio C. Barrionuevo da Luz", {
        "twitter": "@luzfcb",
        "github": "luzfcb"
    }),
    ("Marcos Thomaz", {
        "twitter": "@marcosthomazs",
        "github": "thomazs",
        "site": {
            "nome": "Marcos Thomaz da Silva",
            "href": "https://br.linkedin.com/in/marcosthomaz",
        }
    }),
    ("Felipe Colen", {
        "twitter": "@felipecolen",
        "github": "felipecolen",
        "site": {
            "nome": "Felipe Oliveira Colen",
            "href": "https://br.linkedin.com/in/felipecolen",
        }
    }),
    ("Marcos Duran", {
        "twitter": "@mdzain",
        "github": "zapduran",
        "site": {
            "nome": "Marcos Duran",
            "href": "http://www.mdzain.com/",
        }
    }),
    ("Breno Thales", {
        "twitter": "@brenothales",
        "github": "brenothales",
        "site": {
            "nome": "Breno Thales",
            "href": "https://br.linkedin.com/in/breno-thales-2aa8631b/pt",
        }
    }),
    ("João Soares", {
         "github": "joaosr",
         "twitter": "@joao_mnl"
    }),
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "A comunidade PyNorte se comunica através de mailing " +\
                    "lists, grupo no telegram e ocasionalmente são " +\
                    "promovidos encontros diversos, como almoços, " +\
                    "<em>coding dojos</em>, hangouts e palestras. ",
                "buttons": [
                     {
                         "text": "Blog",
                         "href": "blog",
                     },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade PyNorte inicia sua organização, mas já possui alguns " +\
                        "colaboradores, responsáveis por organizar " +\
                        "eventos, manter a comunicação ativa, divulgar eventos, " +\
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Entre em Contato",
                "icon": "fa-paper-plane",
                "text": "Deseja participar? Sugerir uma atividade ou simplesmente acompanhar o grupo?"
                        " Contacte-nos via Telegram.",
                "buttons": [
                    {
                        "text": "Telegram",
                        "href": "https://telegram.me/joinchat/COYq6QM8RkebVUVK1WxRHQ",
                    },
                ]
            },
            {
                "title": "Hangouts",
                "icon": "fa-wechat",
                "text": "Realizados no primeiro sábado de cada mês. "
                        "Nós organizamos e apresentamos temas diversos relacionados com Python."
                        " Participe!",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "blog/terceiro-hangout/",
                    },
                ],
            },
        ]
    },

    # {
    #     "color": "blue-grey lighten-4",
    #     "title": "Nosso Projetos",
    #     "items": [
    #         {
    #         "title": "MIG-29",
    #         "icon": "fa-fighter-jet",
    #         "text": "MIG-29 é um caça Russo cujo projeto original visava" +\
    #                 "superar o F-22 Raptor",
    #         "buttons": [
    #                 {
    #                     "text": "Código Fonte",
    #                     "href": "#",
    #                 },
    #                 {
    #                     "text": "Wiki",
    #                     "href": "#",
    #                 },
    #             ]
    #         },
    #         {
    #         "title": "SNES",
    #         "icon": "fa-gamepad",
    #         "text": "O Super Nintendo Entertainment Systems visa superar" +\
    #                 "o sucesso de seu antecessor, o NES.",
    #         "buttons": [
    #                 {
    #                     "text": "Site",
    #                     "href": "#",
    #                 },
    #                 {
    #                     "text": "Comprar",
    #                     "href": "#",
    #                 },
    #             ]
    #         }
    #     ]
    # },
    # {
    #     "color": "blue-grey lighten-5",
    #     "title": "Entre em Contato",
    #     "items": [
    #         {
    #         "title": "",
    #         },
    #         {
    #         "icon": "fa-envelope",
    #         "buttons": [
    #                 {
    #                     "text": "Envie um e-mail!",
    #                     "href": "#",
    #                 },
    #             ]
    #         }
    #     ]
    # }
]  # end MALT_HOME

PLUGINS = PLUGINS + [
     'pelican_youtube',
 ]

from themes.malt.functions import *
