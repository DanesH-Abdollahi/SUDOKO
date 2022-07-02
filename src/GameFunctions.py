from InitialValues import *


def is_valid(tmp, solution):
    for i in range(9):
        for j in range(9):
            if tmp[i][j] != 0 and tmp[i, j] != solution[i, j]:
                return False
    return True


def hint_func(screen, position, temp, tmp_color, solution, rects, Horizental_diff, Vertical_diff):

    font = pygame.font.SysFont('Comic Sans MS', 70)
    i, j = position[1], position[0]
    i, j = (i-Margin) // Vertical_diff, (j-Margin) // Horizental_diff

    if i > 8 or j > 8:
        return temp

    if(temp[i, j] != 0 and tmp_color[i][j] == GREEN):
        return temp

    pos = rects[9*i + j].center
    text = str(solution[i, j])
    temp[i, j] = solution[i, j]
    img = font.render(text, True, GREEN)
    pos = img.get_rect(center=pos)
    screen.blit(img, pos)
    pygame.display.update()
    return temp


def is_solved(curr_sudoku, solution):
    if curr_sudoku.tolist() == solution.tolist():
        return True
    return False
