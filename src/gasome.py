import requests

class Gasome:
	def __init__(self):
		self.api = "https://api.gasome.com"
		self.headers = {
			"user-agent": "Android"
		}

	def login(self, username: str, password: str):
		data = {
			"password": password,
			"username": username
		}
		response = requests.post(
			f"{self.api}/v1_2/newLogin",
			data=data,
			headers=self.headers).json()
		if "token" in response["data"]:
			self.access_token = response["data"]["token"]
			self.headers["authorization"] = f"Bearer {self.access_token}"
			self.user_id = self.get_current_user()["data"]["id"]
		return response

	def sign_up(
			self,
			email: str,
			name: str,
			password: str,
			username: str):
		data = {
			"email": email,
			"name": name,
			"password": password,
			"username": username
		}
		return requests.post(
			f"{self.api}/v1_2/users/signup",
			data=data,
			headers=self.headers).json()

	def get_current_user(self):
		return requests.get(
			f"{self.api}/v1_2/user",
			headers=self.headers).json()

	def get_posts(self, page: int = 1, is_global: bool = False):
		return requests.get(
			f"{self.api}/v1_2/getPosts?page={page}&global={is_global}",
			headers=self.headers).json()

	def get_notifications(self, page: int = 1):
		return requests.get(
			f"{self.api}/v1_2/notifications?page={page}",
			headers=self.headers).json()

	def get_trends(self):
		return requests.get(
			f"{self.api}/v1_2/getTrends",
			headers=self.headers).json()

	def get_message_box(self, page: int = 1):
		return requests.get(
			f"{self.api}/v1_2/messagebox?page={page}",
			headers=self.headers).json()

	def get_platforms(self):
		return requests.get(
			f"{self.api}/v1_2/getPlatforms",
			headers=self.headers).json()

	def get_recommended_users(self):
		return requests.get(
			f"{self.api}/v1_2/recommendedUsers",
			headers=self.headers).json()

	def get_user_info(self, username: str):
		return requests.get(
			f"{self.api}/v1_2/info?selected_user={username}",
			headers=self.headers).json()

	def follow_user(self, username: str):
		data = {
			"selected_user": username
		}
		return requests.post(
			f"{self.api}/v1_2/follow",
			data=data,
			headers=self.headers).json()

	def unfollow_user(self, username: str):
		data = {
			"selected_user": username
		}
		return requests.post(
			f"{self.api}/v1_2/follow",
			data=data,
			headers=self.headers).json()

	def get_user_played(self, user_id: int, page: int = 1):
		return requests.get(
			f"{self.api}/v1_2/played?userId={user_id}&page={page}",
			headers=self.headers).json()

	def get_user_posts(self, user_id: int, page: int = 1):
		return requests.get(
			f"{self.api}/v1_2/getPostsByUser?userId={user_id}&page={page}",
			headers=self.headers).json()

	def get_user_old_streams(self, user_id: int):
		return requests.get(
			f"{self.api}/v1_2/oldStreams?userId={user_id}",
			headers=self.headers).json()

	def get_user_followers(self, user_id: int, page: int = 1):
		return requests.get(
			f"{self.api}/v1_2/getFollowers?userId={user_id}&page={page}",
			headers=self.headers).json()

	def get_user_followings(self, user_id: int, page: int = 1):
		return requests.get(
			f"{self.api}/v1_2/getFollowing?userId={user_id}&page={page}",
			headers=self.headers).json()

	def send_message(self, user_id: str, text: str):
		data = {
			"contact_id": user_id,
			"text": text
		}
		return requests.post(
			f"{self.api}/v1_2/conversation/send",
			data=data,
			headers=self.headers).json()

	def create_post(self, text: str):
		data = {
			"text": text
		}
		return requests.post(
			f"{self.api}/v1_2/newPost",
			data=data,
			headers=self.headers).json()

	def edit_profile(
			self,
			name: str = None,
			username: str = None,
			bio: str = None,
			email: str = None,
			website: str = None):
		data = {}
		if name:
			data["name"] = name
		if username:
			data["username"] = username
		if bio:
			data["bio"] = bio
		if email:
			data["email"] = email
		if website:
			data["website"] = website
		return requests.post(
			f"{self.api}/v1_2/postUpdateProfile",
			data=data,
			headers=self.headers).json()

	def change_password(self, old_password: str, new_password: str):
		data = {
			"newPassword": new_password,
			"password": old_password
		}
		return requests.post(
			f"{self.api}/v1_2/updatePassword",
			data=data,
			headers=self.headers).json()

	def get_blocked_users(self):
		return requests.get(
			f"{self.api}/v1_2/blockedUsers",
			headers=self.headers).json()

	def get_conversation(self, user_id: str):
		return requests.get(
			f"{self.api}/v1_2/conversation/{user_id}",
			headers=self.headers).json()

	def search_user(self, query: str):
		return requests.get(
			f"{self.api}/v1_2/getSearchUser?search={query}",
			headers=self.headers).json()

	def search_tag(self, query: str):
		return requests.get(
			f"{self.api}/v1_2/getSearchTag?search={query}",
			headers=self.headers).json()

	def search_game(self, query: str):
		return requests.get(
			f"{self.api}/v1_2/getSearchGame?search={query}",
			headers=self.headers).json()

	def get_post_info(self, post_id: int):
		return requests.get(
			f"{self.api}/v1_2/getPostById?postId={post_id}",
			headers=self.headers).json()

	def like_post(self, post_id: int):
		data = {
			"postId": post_id
		}
		return requests.post(
			f"{self.api}/v1_2/postLike",
			data=data,
			headers=self.headers).json()

	def unlike_post(self, post_id: int):
		data = {
			"postId": post_id
		}
		return requests.post(
			f"{self.api}/v1_2/postLike",
			data=data,
			headers=self.headers).json()

	def delete_post(self, post_id: int):
		data = {
			"postId": post_id
		}
		return requests.post(
			f"{self.api}/v1_2/deletePost",
			data=data,
			headers=self.headers).json()

	def send_report(
			self,
			type: str,
			post_id: int = None,
			user_id: int = None):
		data = {
			"type": type
		}
		if type == "user":
			data["userId"] = user_id
		elif type == "post":
			data["postId"] = post_id
		return requests.post(
			f"{self.api}/v1_2/postReport",
			data=data,
			headers=self.headers).json()

	def get_trend_topics(self, weekly: bool = False):
		return requests.get(
			f"{self.api}/v1_2/getTrendTopics?weekly={weekly}",
			headers=self.headers).json()

	def get_streams(self):
		return requests.get(
			f"{self.api}/v1_2/streams",
			headers=self.headers).json()

	def delete_stream(self, stream_id: int):
		data = {
			"id": stream_id
		}
		return requests.post(
			f"{self.api}/v1_2/deleteStream",
			data=data,
			headers=self.headers).json()

	def get_twitch_user(self, twitch_user_id: str):
		return requests.get(
			f"{self.api}/v1_2/getTwitchUser?userId={twitch_user_id}",
			headers=self.headers).json()	

	def get_live_stream(self, twitch_user_id: str):
		return requests.get(
			f"{self.api}/v1_2/getLiveStream?userId={twitch_user_id}",
			headers=self.headers).json()

	def block_user(self, user_id: int = None, username: str = None):
		data = {}
		if user_id:
			data["userId"] = user_id
		elif username:
			data["username"] = username
		return requests.post(
			f"{self.api}/v1_2/block",
			data=data,
			headers=self.headers).json()


	def unblock_user(self, user_id: int = None, username: str = None):
		data = {}
		if user_id:
			data["userId"] = user_id
		elif username:
			data["username"] = username
		return requests.post(
			f"{self.api}/v1_2/unblock",
			data=data,
			headers=self.headers).json()
