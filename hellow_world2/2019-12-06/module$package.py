import calc.add
import report.table
import sys
import math
#패키지
# - 대규모의 프로젝트를 수행하려면 이미 잘 만들어놓은 코드를 활용하는 것이
# 좋다.
# - 처음부터 모든 코드를 다 작성할 수는 없고 그럴 필요도 없다.
# - 잘 구축된 도구를 적극적으로 활용해야 하며 이런 목적으로 마련된 장치가
# 모듈이다.
# - 모듈의 수가 많아지면 관리하기가 어렵다
# - 모듈을 관리하기 위해 패키지라는 개념이 필요하다.
# - 모듈이 파일이라면 패키지는 폴더와 같다.
#  즉 모듈 파일을 관리 하기 위한 폴더
calc.add.outadd(1, 2)
report.table.print_report()

print(sys.builtin_module_names) # 지금 시스템에서 쓸수있는 모듈 네임
print(dir(math)) # math 안에서 쓸수 있는것들 나열