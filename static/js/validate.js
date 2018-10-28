function validacao() {

			if (document.form.matricula.value == "") {
				alert("O campo matrícula não pode ficar vazio!");
				document.form.matricula.focus();
				return false;
			}

			if (document.form.password.value == "") {
				alert("O campo senha não pode ficar vazio!");
				document.form.password.focus();
				return false;
			}

		return true;
	}
