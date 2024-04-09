import subprocess

def run_pytest():
    try:
        test_files_path = r"C:\Users\Дмитрий\PycharmProjects\pythonProject4\test_bankxyz"
        subprocess.run(["pytest", "--alluredir=allure-results"], check=True, cwd=test_files_path)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка {e}")
    except Exception as ex:
        print(f"Ошибка {ex}")

def generate_allure_report():
    allure_path = r"C:\Users\Дмитрий\PycharmProjects\pythonProject4\config\allure\allure-2.27.0\bin"
    results_path = r"C:\Users\Дмитрий\PycharmProjects\pythonProject4\test_bankxyz\allure-results"
    report_path = r"C:\Users\Дмитрий\PycharmProjects\pythonProject4\test_bankxyz\allure-report"

    # Запуск тестов
    run_pytest()
    # Генерация отчета
    subprocess.run(["allure.bat", "generate", results_path, "-o", report_path], shell=True, cwd=allure_path)
    # Открытие отчета в браузере
    subprocess.run(["allure.bat", "open", report_path], shell=True, cwd=allure_path)

if __name__ == "__main__":
    generate_allure_report()