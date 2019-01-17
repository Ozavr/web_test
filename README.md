web_test

pip install -r requirements.txt
Чтобы протестировать систему, обновоите настройки postgres и redis на ваши

cd web_test
sudo ./entrypoint.sh


Ограничения!
Работает только под Linux и MacOs (для пораждения процессов использует fork)