
    from django.test import RequestFactory
    from django.http import HttpResponse

    factory = RequestFactory()

    def test_returns_http_response_object(self):
        request = factory.get('/confirmar_recuperar_contrasena/')
        response = confirmar_recuperar_contrasena(request)
        assert isinstance(response, HttpResponse)