class Publisher():
    def publish_image(self, file_name):
        raise NotImplementedError

    def publish_video(self, video_file_name, thumb_file_name):
        raise NotImplementedError

class DummyPublisher(Publisher):
    def publish_image(self, file_name):
        pass

    def publish_video(self, video_file_name, thumb_file_name):
        pass