from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class CreatePostUserThrottle(UserRateThrottle):
    scope = 'create_post_user'


class CreatePostAnonThrottle(AnonRateThrottle):
    scope = 'create_post_anon'


class ListPostUserThrottle(UserRateThrottle):
    scope = 'list_post_user'


class ListPostAnonThrottle(AnonRateThrottle):
    scope = 'list_post_anon'


class RetrievePostUserThrottle(UserRateThrottle):
    scope = 'retrieve_post_user'


class RetrievePostAnonThrottle(AnonRateThrottle):
    scope = 'retrieve_post_anon'


class UpdatePostUserThrottle(UserRateThrottle):
    scope = 'update_post_user'


class UpdatePostAnonThrottle(AnonRateThrottle):
    scope = 'update_post_anon'


class DeletePostUserThrottle(UserRateThrottle):
    scope = 'delete_post_user'


class DeletePostAnonThrottle(AnonRateThrottle):
    scope = 'delete_post_anon'
