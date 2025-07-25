class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        cleanv1 = []
        cleanv2 = []

        for s in version1.split('.'):
            temps = s
            while temps[0] == '0' and len(temps) > 1:
                temps = temps[1:]
            cleanv1.append(int(temps))

        for s in version2.split('.'):
            temps = s
            while temps[0] == '0' and len(temps) > 1:
                temps = temps[1:]
            cleanv2.append(int(temps))

        v1len = len(cleanv1)
        v2len = len(cleanv2)
        for i in range(0, max(v1len, v2len)):
            if v1len > i and v2len > i:
                if cleanv1[i] < cleanv2[i]: return -1
                elif cleanv1[i] > cleanv2[i]: return 1
            elif v1len > i:
                if cleanv1[i] > 0: return 1
            elif v2len > i:
                if cleanv2[i] > 0: return -1

        return 0