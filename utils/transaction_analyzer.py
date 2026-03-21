class TransactionAnalyzer:

    def analyze(self, transactions):
        totals = {}

        for transaction in transactions:
            user = transaction["user"]
            amount = transaction["amount"]

            if user in totals:
                totals[user] += amount
            else:
                totals[user] = amount

        top_user = max(totals, key=lambda user: totals[user])

        sorted_users = sorted(totals.items(), key=lambda x: x[1], reverse=True)

        filtered_users = {}

        for user, total in totals.items():
            if total > 150:
                filtered_users[user] = total

        return {
            "totals": totals,
            "top_user": top_user,
            "sorted_users": sorted_users,
            "filtered_users": filtered_users,
        }
