import re


class TextParser:

    @staticmethod
    def parse(message: str) -> dict:

        data = {}

        linhas = message.splitlines()

        for linha in linhas:

            linha = linha.strip()

            if not linha:
                continue

            if linha.lower().startswith("preencher formulário"):
                _, valor = linha.split(":", 1)
                data["formulario"] = valor.strip()
                continue

            match = re.match(r"(.+?):\s*(.+)", linha)

            if match:
                chave = (
                    match.group(1)
                    .strip()
                    .lower()
                    .replace(" ", "_")
                )

                valor = match.group(2).strip()

                data[chave] = valor

        return data