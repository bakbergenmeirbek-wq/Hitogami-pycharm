#1
# with open("shop_logs.txt", "r") as file:
#     lines = file.readlines()
#
# users = set()
# total_purchases = 0
# total_sum = 0
# user_spending = {}
#
# for line in lines:
#     parts = line.strip().split(";")
#
#     date = parts[0]
#     user = parts[1]
#     action = parts[2]
#
#
#     users.add(user)
#
#
#     if action == "BUY":
#         amount = int(parts[3])
#
#         total_purchases += 1
#         total_sum += amount
#
#
#         if user in user_spending:
#             user_spending[user] += amount
#         else:
#             user_spending[user] = amount
#
#
# max_user = ""
# max_spent = 0
#
# for user in user_spending:
#     if user_spending[user] > max_spent:
#         max_spent = user_spending[user]
#         max_user = user
#
#
# if total_purchases > 0:
#     average_check = total_sum / total_purchases
# else:
#     average_check = 0
#
#
# with open("report.txt", "w") as report:
#     report.write(f"Уникальных пользователей: {len(users)}\n")
#     report.write(f"Всего покупок: {total_purchases}\n")
#     report.write(f"Общая сумма: {total_sum}\n")
#     report.write(f"Самый активный покупатель: {max_user}\n")
#     report.write(f"Средний чек: {average_check}\n")
#
# print("Отчёт создан в файле report.txt")

#3
# import json
#
#
# with open("orders.json", "r") as file:
#     orders = json.load(file)
#
# total_revenue = 0
# user_orders = {}
# total_items_sold = 0
# item_frequency = {}
#
# top_user = ""
# max_order_total = 0
#
# for order in orders:
#     user = order["user"]
#     total = order["total"]
#     items = order["items"]
#
#
#     total_revenue += total
#
#
#     if user in user_orders:
#         user_orders[user] += 1
#     else:
#         user_orders[user] = 1
#
#
#     total_items_sold += len(items)
#
#     for item in items:
#         if item in item_frequency:
#             item_frequency[item] += 1
#         else:
#             item_frequency[item] = 1
#
#
#     if total > max_order_total:
#         max_order_total = total
#         top_user = user
#
#
# most_popular_item = max(item_frequency, key=item_frequency.get)
#
#
# summary = {
#     "total_revenue": total_revenue,
#     "top_user": top_user,
#     "most_popular_item": most_popular_item,
#     "total_orders": len(orders)
# }
# with open("summary.json", "w") as file:
#     json.dump(summary, file, indent=4)
#
#
# print("Общая сумма заказов:", total_revenue)
# print("Заказы по пользователям:", user_orders)
# print("Всего продано товаров:", total_items_sold)
# print("Пользователь с самым дорогим заказом:", top_user)
# print("Самый популярный товар:", most_popular_item)

#4
# import csv
# import json
#
# transactions = []
# user_operations = {}
# suspicious_transactions = []
# suspicious_users = set()
# total_suspicious_amount = 0
#
#
# with open("transactions.csv", "r", newline="") as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         user = row["user_id"]
#         amount = int(row["amount"])
#
#
#         transactions.append({"user": user, "amount": amount})
#
#
#         if user in user_operations:
#             user_operations[user] += 1
#         else:
#             user_operations[user] = 1
#
#
#         if amount > 500000:
#             suspicious_transactions.append({"user": user, "amount": amount})
#             total_suspicious_amount += amount
#             suspicious_users.add(user)
#
#
# for user, count in user_operations.items():
#     if count > 3:
#         suspicious_users.add(user)
#
#
# with open("fraud_report.txt", "w") as report:
#     report.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
#     report.write(f"Подозрительных пользователей: {len(suspicious_users)}\n")
#     report.write(f"Список пользователей: {list(suspicious_users)}\n")
#     report.write(f"Общая сумма подозрительных операций: {total_suspicious_amount}\n")
#
#
# with open("fraud_users.json", "w") as json_file:
#     json.dump(list(suspicious_users), json_file, indent=4)
#
#
# print("Подозрительных транзакций:", len(suspicious_transactions))
# print("Подозрительных пользователей:", len(suspicious_users))
# print("Список подозрительных пользователей:", suspicious_users)
# print("Общая сумма подозрительных операций:", total_suspicious_amount)