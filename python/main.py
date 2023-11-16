import tkinter as tk
import subprocess
import threading

def execute_script(script_name, button):
    try:
        button.config(bg="green")  # Define a cor do botão para verde enquanto o código é executado

        process = subprocess.Popen(["python", script_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                console_output.config(state=tk.NORMAL)
                console_output.insert(tk.END, output)
                console_output.config(state=tk.DISABLED)
                root.update()  # Atualiza a interface para exibir a saída imediatamente

        process.wait()
        if process.returncode == 0:
            status_label.config(text="Executado com sucesso!", fg="green")
        else:
            status_label.config(text="Erro na execução", fg="red")
    except Exception as e:
        console_output.config(state=tk.NORMAL)
        console_output.insert(tk.END, str(e))
        console_output.config(state=tk.DISABLED)
        status_label.config(text="Erro na execução", fg="red")
    finally:
        button.config(bg="SystemButtonFace")  # Restaura a cor original do botão após a execução
        button.config(state=tk.NORMAL)  # Ativa o botão novamente

def execute_script_on_click(script_name, button):
    # Desabilita o botão enquanto o código é executado
    button.config(state=tk.DISABLED)
    thread = threading.Thread(target=execute_script, args=(script_name, button))
    thread.start()

root = tk.Tk()
root.title("Executar Arquivo Python")

# Crie um Frame para organizar os botões em duas linhas
button_frame = tk.Frame(root)
button_frame.pack()

# Crie botões para diferentes scripts
button1 = tk.Button(button_frame, text="Baixa imagens", command=lambda: execute_script_on_click("baixa imagens.py", button1))
button2 = tk.Button(button_frame, text="Lista nomes das pastas", command=lambda: execute_script_on_click("lista nomes das pastas.py", button2))
button3 = tk.Button(button_frame, text="Compara arquivo", command=lambda: execute_script_on_click("compara arquivo.py", button3))
button4 = tk.Button(button_frame, text="Transforma 250 por 250", command=lambda: execute_script_on_click("transforma250.py", button4))
button5 = tk.Button(button_frame, text="Remove os numeros", command=lambda: execute_script_on_click("tira numero.py", button5))
button6 = tk.Button(button_frame, text="Enviar arquivos", command=lambda: execute_script_on_click("envia.py", button6))

# Use grid para organizar os botões em duas linhas e duas colunas
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=1, column=0, padx=10, pady=10)
button4.grid(row=1, column=1, padx=10, pady=10)
button5.grid(row=2, column=0, padx=10, pady=10)
button6.grid(row=2, column=1, padx=10, pady=10)
console_output = tk.Text(root, wrap=tk.WORD, width=100, height=20)
console_output.pack()
console_output.config(state=tk.DISABLED)

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

root.mainloop()
