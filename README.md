GetOTP Python Library

## Quickstart

Add `getotp` to `INSTALLED_APPS` settings:-

```
NSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "getotp",
    ...
```

Add to `AUTHENTICATION_BACKENDS`:

```
AUTHENTICATION_BACKENDS = [
  "django.contrib.auth.backends.ModelBackend",
  "some.other.auth.OtherBackend",
  ...,
  "getotp.auth.GETOTPBackend",
]
```

Add to `urls.py`:-

```
urlpatterns = [
    path("", views.index),
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="auth")),
    ...
    path("getotp/", include("getotp.urls")),
    ...
]
```

Run `migrate`.

The login button should be available under https://yoursite.com/getotp/login/start/.

## Sending OTP
To send OTP, we can use `send_otp()` function from `getotp.client` module:-

```
from getotp.client import send_otp

otp = send_otp("email",
                success_redirect_url=settings.GETOTP_LOGIN_SUCCESS_REDIRECT,
                fail_redirect_url=settings.GETOTP_LOGIN_FAIL_REDIRECT,
                callback_url=settings.GETOTP_CALLBACK,
            )
if otp.ok:
    return redirect(otp.link)
else:
    print(otp.errors)
```
