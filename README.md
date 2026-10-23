# Insportify

A Django sports-event application connecting participant and organization profiles with event discovery, availability, venues and booking workflows.

## Implemented areas

- Email-based custom user model, individual profiles and organization profiles.
- Sports categories, sports types, positions and skill preferences.
- Event creation, discovery, invitations and event details.
- Participant and organization availability.
- Venue and location data.
- Cart, order records and Stripe charge-related views.

Event matching includes application-side filtering. Do not describe it as a trained ML recommender unless a separate model and evaluation are identified.

## Architecture and navigation

| Path | Responsibility |
| --- | --- |
| `Insportify/settings.py` | Django application, database and service configuration |
| `Insportify/urls.py` | Root URL routing |
| `EventsApp/models.py` | User, event, availability, venue, cart and order entities |
| `EventsApp/urls.py` | Event, profile, availability and payment routes |
| `EventsApp/views.py` | Application workflows and integrations |
| `UserRegister/` | Registration-related application code |
| `requirements.txt` | Historical Python dependency list |

The custom authentication model is `EventsApp.User`. Data uses PostgreSQL in the checked-in settings. Requests flow through Django URL routing into views, with Django models handling persistence and server-rendered templates supplying the interface.

## Local setup checklist

This is a historical project, not a turnkey production deployment. Use a disposable local environment and synthetic data.

1. Review the pinned dependencies in `requirements.txt` and select a compatible Python/PostgreSQL environment. Upgrade and validate old packages before exposing the application publicly.
2. Review `Insportify/settings.py` and application integrations. Replace environment-specific configuration with your own local settings. Never copy service credentials into a README or commit.
3. Configure an empty local PostgreSQL database and local email delivery. Use Stripe test mode only when testing payment flows.
4. Install reviewed dependencies in a virtual environment, then run:

```sh
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

Dependency installation and full application execution have not been validated by this documentation-only change. Do not treat these commands as proof that every historical dependency works on a current runtime.

## Testing priorities

`EventsApp/tests.py` currently contains only the Django test placeholder. Before calling the project production-ready, add coverage for:

- User creation, registration and object-level access control.
- Event ownership, invitations and profile updates.
- Availability overlap, recurrence and date/time boundaries.
- Cart totals and server-side price validation.
- Payment success, cancellation, duplicate callbacks and failure recovery using mocks or Stripe test mode.

Never test with real payment details, real participant records or live charges. Confirm the intended behavior from the source and requirements rather than treating the checklist as implemented functionality.

## Production-readiness review

Review debug settings, allowed hosts, secret management, database/email configuration, upload validation, authorization, CSRF handling, payment idempotency and dependency support. The current source should be audited before any public deployment. Historical configuration or credentials found in a repository must not be reused; if real credentials were ever committed, rotate them through the provider and review history separately.

This project demonstrates a connected full-stack business workflow. It does not, by itself, establish deployment scale, security certification or individual authorship of every component.
