import sys
import re
from z3 import Optimize, Int, Sum, sat


def main() -> None:
    manual = open(sys.argv[1]).read().splitlines()
    total = 0

    for line in manual:
        pattern = re.search(r'\{([^}]*)\}', line)
        targets = [int(x) for x in pattern.group(1).split(',')]
        N = len(targets)

        button_groups = re.findall(r'\(([^)]*)\)', line)

        effects = []
        for grp in button_groups:
            effect = [0] * N
            indices = [int(x) for x in grp.split(',')]
            for idx in indices: effect[idx] = 1
            effects.append(effect)

        B = len(effects)

        # 1. 해결사(Optimizer) 생성
        opt = Optimize()

        # 2. 변수 생성: 각 버튼을 누르는 횟수 (정수)
        x = [Int(f'x_{j}') for j in range(B)]

        # 3. 제약 조건 추가
        for j in range(B):
            opt.add(x[j] >= 0)

        # 각 카운터(row)마다 목표값을 맞춰야 함
        # 식: (버튼0 * 효과) + (버튼1 * 효과) + ... == 목표값
        for i in range(N):
            opt.add(Sum(x[j] * effects[j][i] for j in range(B)) == targets[i])

        # 4. 목표 설정: 버튼 누른 총 횟수(Sum(x))를 최소화(Minimize) 하라
        total_presses = Sum(x)
        opt.minimize(total_presses)

        # 5. 풀기
        if opt.check() == sat:
            model = opt.model()
            total += model.evaluate(total_presses).as_long()
        else:
            raise ValueError("No solution found")

    print(total)


if __name__ == "__main__":
    main()
