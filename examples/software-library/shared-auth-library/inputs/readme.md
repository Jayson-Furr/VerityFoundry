# SharedAuth

SharedAuth wraps OAuth-style login flows, access-token refresh, service-token
exchange, role lookup, and audit event emission.

Planned package surfaces:

- `loginWithRedirect`
- `exchangeAuthorizationCode`
- `refreshAccessToken`
- `getCurrentUser`
- `getUserRoles`
- `emitAuthAuditEvent`

Open questions:

- Supported languages are not final.
- Token storage policy is not final.
- Required identity providers are not final.
- Data retention and audit requirements need security review.
- Public versus internal API boundaries are not approved.
