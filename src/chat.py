from search import search_prompt
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Enviar uma pergunta para o search e retornar a resposta.")
    parser.add_argument("question", nargs="?", help="Pergunta a ser enviada. Se ausente, será lida da entrada padrão.")
    args = parser.parse_args()

    if args.question:
        question = args.question
    else:
        if sys.stdin.isatty():
            try:
                question = input("Digite a pergunta (ou use: python src/chat.py \"sua pergunta\"): ").strip()
            except EOFError:
                question = ""
        else:
            question = sys.stdin.read().strip()

    if question and ((question.startswith('"') and question.endswith('"')) or (question.startswith("'") and question.endswith("'"))):
        question = question[1:-1].strip()

    if not question:
        print("Nenhuma pergunta fornecida. Encerrando.")
        return

    try:
        result = search_prompt(question)
    except Exception as e:
        print(f"Erro ao executar search_prompt: {e}")
        return

    if not result:
        print("Nenhuma resposta retornada pelo search.")
        return

    try:
        content = getattr(result, "content", None) or result
        print(content)
    except Exception:
        print(result)


if __name__ == "__main__":
    main()