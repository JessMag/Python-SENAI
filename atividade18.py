#Crie um formulário em Tkinter, contendo, nome, idade, e-mail, endereço, celular.
#Problema: Sistema de Cadastro de Clientes

#Você é um desenvolvedor de software e foi contratado por uma empresa de serviços para criar um sistema de cadastro de clientes. O sistema deve permitir que os clientes forneçam suas informações pessoais, como nome, idade, e-mail, endereço e celular.

#Atividade:
#Crie um formulário em Tkinter que contenha os seguintes campos:
#Nome
#Idade
#E-mail
#Endereço
#Celular
#O formulário deve ter um botão de "Enviar" que, quando clicado, imprima as informações do cliente na console.

#Restrições:
#O formulário deve ser criado usando Tkinter.
#O código deve ser escrito em Python.

import tkinter as tk


def mostrar_info():
    info = [input1.get(),]
    lb_mostra_info.config(text=info)



tela  =  tk.Tk()
tela.geometry('1750x3750')
tela.title('Cadastro de Clientes')

label_titulo = tk.Label(tela, text='Sistema de Cadastro de Clientes', fg='white', bg='navy blue', font=('calibri', 15))
label_titulo.grid(row=1, column=4, padx=10)

label1 = tk.Label(tela, text='Nome:', fg='black', font=('calibri', 10))
label1.grid(row=2, column=1, padx=10)
input1 = tk.Entry(tela, fg='white',font=('arial',15), bg='grey')
input1.grid(row=2, column=2, padx=10, pady=10)

label2 = tk.Label(tela, text='Idade:', fg='black', font=('calibri', 10))
label2.grid(row=3, column=1, padx=10)
input2 = tk.Entry(tela, fg='white',font=('arial',15), bg='grey')
input2.grid(row=3, column=2, padx=10, pady=10)

label3 = tk.Label(tela, text='Email:', fg='black', font=('calibri', 10))
label3.grid(row=4, column=1, padx=10)
input3 = tk.Entry(tela, fg='white',font=('arial',15), bg='grey')
input3.grid(row=4, column=2, padx=10, pady=10)

label4 = tk.Label(tela, text='Endereço:', fg='black', font=('calibri', 10))
label4.grid(row=5, column=1, padx=10)
input4 = tk.Entry(tela, fg='white',font=('arial',15), bg='grey')
input4.grid(row=5, column=2, padx=10, pady=10)

label5 = tk.Label(tela, text='Celular:', fg='black', font=('calibri', 10))
label5.grid(row=6, column=1, padx=10)
input5 = tk.Entry(tela, fg='white',font=('arial',15), bg='grey')
input5.grid(row=6, column=2, padx=10, pady=10)


botao_enviar = tk.Button(tela, text='Enviar', font=('Calibri',15), fg='white', bg='navy blue', command=mostrar_info)
botao_enviar.grid(row=7, column=3, padx=10, pady=10)
tela.bind("<Return>", lambda event: mostrar_info())

lb_mostra_label = tk.Label(tela, text='', fg='blue', font=('calibri', 15))
lb_mostra_label.grid(row=8, column=1, padx=10, pady=10)


lb_mostra_info = tk.Label(tela, text='', fg='blue', font=('calibri', 15))
lb_mostra_info.grid(row=8, column=2, padx=10, pady=10)




tela.mainloop()