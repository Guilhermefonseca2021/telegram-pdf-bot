from app.forms import FORMS


class FormValidator:

    @staticmethod
    def validate(data: dict):

        nome_formulario = data.get("formulario")

        if not nome_formulario:
            raise ValueError("Formulário não informado.")

        formulario = FORMS.get(nome_formulario)

        if not formulario:
            raise ValueError(f"Formulário '{nome_formulario}' não encontrado.")

        campos_faltando = []

        for campo in formulario["required"]:
            valor = data.get(campo)

            if valor is None or valor.strip() == "":
                campos_faltando.append(campo)

        return {
            "valid": len(campos_faltando) == 0,
            "missing": campos_faltando,
            "form": formulario
        }