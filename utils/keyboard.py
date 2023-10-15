from services.interfaces import SelectCD


def make_double_keyboard(lst: list) -> list:
    matrix = []

    if len(lst) % 2 == 0:
        for i in range(0, len(lst), 2):
            matrix.append([lst[i], lst[i + 1]])
    else:
        for i in range(0, len(lst) - 1, 2):
            matrix.append([lst[i], lst[i + 1]])
            
        matrix.append([lst[-1]])

    return matrix


def select_points(callback) -> int:
    count_selected = 0
    was_unselect = False

    pressed_callback_data = SelectCD.unpack(callback.data)
    inline_keyboard = callback.message.reply_markup.inline_keyboard

    for i in range(len(inline_keyboard)):
        for j in range(len(inline_keyboard[i])):
            try:
                callback_data = SelectCD.unpack(inline_keyboard[i][j].callback_data)
                if callback_data.is_selected:
                    count_selected += 1
            except:
                pass
            
            else:
                print(callback_data)
                if callback_data == pressed_callback_data:

                    if not callback_data.is_selected:
                        inline_keyboard[i][j].text += " ✅"
                        callback_data.is_selected = True

                    else:
                        inline_keyboard[i][j].text = inline_keyboard[i][j].text.replace(" ✅", "")
                        callback_data.is_selected = False
                        was_unselect = True

                    inline_keyboard[i][j].callback_data = callback_data.pack()

    if count_selected == 1 and was_unselect:
        return inline_keyboard, -1
    elif count_selected == 0:
        return inline_keyboard, 1
    else:
        return inline_keyboard, 0  