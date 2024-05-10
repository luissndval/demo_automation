# Comando para crear el feature
behave features

# Comando para ejecutar la prueba y generar el reporte de Allure
behave -f allure_behave.formatter:AllureFormatter -o reports/

behave -f allure_behave.formatter:AllureFormatter -o reports/ [--tags=@declarado]

# Comando para levantar el servidor de pruebas con el reporte de Allure
allure serve reports/

# Instalar los plugins requeridos (agregar cualquier otro si es necesario)
pip install -r requirements.txt

# Convertir el reporte de Allure en formato HTML
allure generate reports/ -c -o reports/html/

#Instalar Requirements
python install_requirements.py
