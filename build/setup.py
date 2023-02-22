#!/usr/bin/env python

from distutils.core import setup, Extension


_modules = Extension('_qAgenda',
                           sources=['qAgenda_wrap.c', 'qAgenda.c', 'listas.c'],
                           )

setup (name = 'qAgenda',
       version = '0.1',
       author      = "J.F.C. Rodrigues",
       description = """Um projeto de um sistema de cadastro e gerenciamento para a materia de Algoritmo de Estrutura de Dados do INF-UFG""",
       ext_modules = [_modules],
       py_modules = ["qAgenda"],
       )
