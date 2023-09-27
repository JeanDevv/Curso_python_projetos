one_note_student = float(input("1ª nota da avaliação: ".strip()))
two_note_student = float(input("2ª nota da avaliação: ".strip()))
average_student = (one_note_student + two_note_student) / 2 #calculando a média das notas do aluno
colors_palette = {"green": "\033[32m", "red": "\033[31m", "yellow": "\033[33m", "end_color": "\033[m"} #variável com paleta de cores para cor da letra
print("O aluno tem as notas {:.1f} e {:.1f} a média do aluno é {:.1f}!".format(one_note_student, two_note_student, average_student))
if average_student < 5.0:
    print("O aluno está {}REPROVADO{}!".format(colors_palette["red"], colors_palette["end_color"]))
elif average_student >= 5.0 and average_student < 7:
    print("O aluno está de {}RECUPERAÇÃO{}!".format(colors_palette["yellow"], colors_palette["end_color"]))
elif average_student >= 7.0:
    print("O aluno está {}APROVADO{}!".format(colors_palette["green"], colors_palette["end_color"]))
