from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from website.models import Funcionario

class FuncionarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Funcionario.objects.create(
            nome='NomeTeste', 
            sobrenome='SobrenomeTeste', 
            cpf='12345678901',
            tempo_de_servico=2,
            remuneracao=2500.00,
            cdp='CDPTeste'
        )

    def test_nome_content(self):
        funcionario = Funcionario.objects.get(id=1)
        expected_nome = f'{funcionario.nome}'
        self.assertEqual(expected_nome, 'NomeTeste')

    def test_sobrenome_content(self):
        funcionario = Funcionario.objects.get(id=1)
        expected_sobrenome = f'{funcionario.sobrenome}'
        self.assertEqual(expected_sobrenome, 'SobrenomeTeste')

    def test_cpf_content(self):
        funcionario = Funcionario.objects.get(id=1)
        expected_cpf = f'{funcionario.cpf}'
        self.assertEqual(expected_cpf, '12345678901')

    def test_tempo_de_servico_content(self):
        funcionario = Funcionario.objects.get(id=1)
        expected_tempo_de_servico = funcionario.tempo_de_servico
        self.assertEqual(expected_tempo_de_servico, 2)

    def test_remuneracao_content(self):
        funcionario = Funcionario.objects.get(id=1)
        expected_remuneracao = funcionario.remuneracao
        self.assertEqual(expected_remuneracao, 2500.00)

    def test_cdp_content(self):
        funcionario = Funcionario.objects.get(id=1)
        expected_cdp = f'{funcionario.cdp}'
        self.assertEqual(expected_cdp, 'CDPTeste')
class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.cadastro_url = reverse('cadastro')
        self.login_url = reverse('login')
        self.home_url = reverse('home')

    def test_cadastro_GET(self):
        response = self.client.get(self.cadastro_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro/cadastro.html')

    def test_cadastro_POST(self):
        response = self.client.post(self.cadastro_url, {
            'usuario': 'novo_usuario',
            'email': 'novo_email@example.com',
            'senha': 'nova_senha'
        })

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_login_POST(self):
        user = User.objects.create_user(username='testuser', password='12345')

        response = self.client.post(self.login_url, {
            'usuario': 'testuser',
            'senha': '12345'
        })
