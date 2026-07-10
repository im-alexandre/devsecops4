package main

import rego.v1

deny contains msg if {
  input.debug == true
  msg := "debug deve estar desativado"
}

deny contains msg if {
  input.require_auth == false
  msg := "autenticacao deve ser obrigatoria"
}

deny contains msg if {
  input.allow_shell_diagnostics == true
  msg := "diagnostico por shell nao deve ser permitido"
}

deny contains msg if {
  input.database.allow_raw_sql == true
  msg := "SQL bruto nao deve ser permitido"
}
