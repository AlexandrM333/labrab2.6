#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    school = {
            '1а': 23,
            '1б': 22,
            '2а': 19,
            '2б': 20,
            '3в': 22,
            '3г': 20,
            '4а': 23,
            '4г': 24,
            '5б': 19,
            '5в': 18,
            '6а': 21,
            '6г': 23,
            '7а': 22,
            '7б': 22,
            '8а': 21,
            '8б': 23,
            '9а': 18,
            '9в': 21,
            '10в': 16,
            '10г': 15,
            '11а': 17,
            '11б': 15,
        }

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'change':
            klass = input("Выберите класс:")
            new_num = input("Новое количество учащихся?:")
            school[klass] = int(new_num)

        elif command == 'add':
            new_klass = input("Новый класс: ")
            number_new_klass = input("Количество учащихся?: ")
            school[new_klass] = number_new_klass

        elif command == 'list':
            for key in sorted(school.keys()):
                print(key + ": " + str(school[key]))

        elif command == 'delete':
            klass = input("Выберите класс:")
            school.pop(klass)
            print("Класс удален")

        elif command == "total":
            total = 0
            for key in school:
                total += int(school[key])
            print(total, "учащихся")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить класс;")
            print("list - список классов;")
            print("change - изменить класс")
            print("delete - удалить класс;")
            print("sum - количество учащихся;")
            print("help - справка;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
