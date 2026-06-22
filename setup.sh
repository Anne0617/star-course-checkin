#!/bin/bash
set -e
echo "=== 正在安装十五五闯关系统 ==="

# 安装依赖
apt-get update -q
apt-get install -y -q python3-pip python3-venv git

# 克隆代码
cd /opt
git clone https://github.com/Anne0617/star-course-checkin.git
cd star-course-checkin/backend

# 设置 Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -q

# 初始化数据库
python3 manage.py migrate --run-syncdb

# 创建管理员
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin','admin@star.com','admin123') if not User.objects.filter(username='admin').exists() else None"

# 启动服务（后台运行）
nohup gunicorn nebula.wsgi:application -b 0.0.0.0:8000 --workers 2 > /var/log/star-course.log 2>&1 &

echo "=== 部署完成！==="
echo "访问地址: http://$(curl -s ifconfig.me):8000/"
echo "后台地址: http://$(curl -s ifconfig.me):8000/admin/"
echo "管理员账号: admin / admin123"