from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visit = [False] * len(accounts)
        result = []

        mail_idx_dic = self.mailIdxToDic(accounts)

        for i, account in enumerate(accounts):
            if visit[i]:
                continue

            name, emails = account[0], set()
            self.dfs(visit, mail_idx_dic, i, emails, accounts)
            result.append([name] + sorted(emails))

        return result

    def mailIdxToDic(self, accounts):
        mail_idx_dic = {}

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                if email in mail_idx_dic:
                    mail_idx_dic[email].append(i)
                else:
                    mail_idx_dic[email] = [i]

        return mail_idx_dic

    def dfs(self, visit, mail_idx_dic, i, emails, accounts):
        if visit[i]:
            return

        visit[i] = True

        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            emails.add(email)

            for neighbor in mail_idx_dic[email]:
                self.dfs(visit, mail_idx_dic, neighbor, emails, accounts)
