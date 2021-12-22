N1, N2, N3, N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / (2 + 3 + 4 + 1)

print("Media: {:.1f}".format(MEDIA))

if MEDIA >= 7:
    print("Aluno aprovado.")
elif MEDIA < 5:
    print("Aluno reprovado.")
elif MEDIA >= 5 and MEDIA <= 6.9:
    print("Aluno em exame.")

    exam_points = float(input())
    print("Nota do exame: {:.1f}".format(exam_points))
    
    final_points = (exam_points + MEDIA) / 2

    if final_points >= 5:
        print("Aluno aprovado.")
    elif final_points <= 4.9:
        print("Aluno reprovado.")

    print("Media final: {:.1f}".format(final_points))
    