# Python Version 3.8
from AssessmentPDFLib import *

rc(multipage=True, name='report.pdf', size='a4')


@report_object(output=True)
@report_complexity(operators=True, operands=False)
def foo():
    print("hello")


if __name__ == "__main__":
    foo()
    report_object = report_object(output=True)(report_object)
    report_object(report_object)
    report_complexity = report_complexity(
        operators=True, operands=False)(report_complexity)(operators=True, operands=False)
    report_complexity(report_complexity)

writeToFile()
