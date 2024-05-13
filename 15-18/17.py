import itertools


def generate_combinations(objects, boxes):
    combinations = list(itertools.combinations(objects.keys(), boxes))
    return combinations


def box_filling(objects, boxes, max_weight_in_box):
    # начальный результат - None.
    result = -1

    # Генерация всех возможных комбинаций раскладки объектов по ящикам.
    for _ in generate_combinations(objects, boxes):
        # Распределение объектов между ящиками.
        boxes_contents = [[] for _ in range(boxes)]
        for i, obj in enumerate(objects):
            boxes_contents[i % boxes].append(obj)

        # Проверка, что вес объектов в каждом ящике не превышает максимально допустимого значения.
        if all([sum([objects[obj] for obj in box]) <= max_weight_in_box for box in boxes_contents]):
            # Если проверка пройдена успешно, сохраняем результат и выходим из цикла.
            result = boxes_contents
            break
    return result


result = -1
boxes = 2
max_weight_in_box = 0.9

objects = {'болты': 0.5, 'гвозди': 0.3, 'шурупы': 0.4, 'инструменты': 0.6}

while box_filling(objects, boxes, max_weight_in_box) == -1 and boxes <= len(objects):
    boxes += 1
    if box_filling(objects, boxes, max_weight_in_box) != -1:
        break
result = box_filling(objects, boxes, max_weight_in_box)

print(result)