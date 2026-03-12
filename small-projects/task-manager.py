# Lista que armazena as tarefas
tasks = []

# Função para adicionar uma nova tarefa
def add_task(task):
    tasks.append(task)
    print(f'Tarefa "{task}" adicionada com sucesso!')

# Função para mostrar todas as tarefas
def show_tasks():
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de tarefas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Função para remover uma tarefa
def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f'Tarefa "{removed}" removida.')
    else:
        print("Índice inválido.")

# Exemplo de uso do programa
add_task("Estudar Python")
add_task("Aprender Machine Learning")
add_task("Praticar GitHub")

show_tasks()

# Removendo uma tarefa
remove_task(1)

show_tasks()