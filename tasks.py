# coding=utf-8

from invoke import task


@task
def pep8(ctx):
  ctx.run("pep8 all_page_login all_page_login_test")


@task
def lint(ctx):
  ctx.run("pylint all_page_login all_page_login_test -r n")


@task
def test(ctx):
  ctx.run("py.test -v --cov all_page_login --cov-report=html --cov-report=term-missing all_page_login_test")


@task(pre=[test, pep8, lint])
def check(ctx):
  pass




