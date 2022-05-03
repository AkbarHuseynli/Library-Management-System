class Mentor:
    def __init__(self,full_name,experience,available_lecture,contact_num):
        self.full_name = full_name
        self.experience = experience
        self.__available_lecture = available_lecture
        self.__contact_num = contact_num

    def get_av_lec(self):
        return self.__available_lecture

    def set_av_lec(self,lec_av):
        self.available_lecture = lec_av

    def get_mentor_number(self):
        return self.__contact_num

    def set_mentor_number(self,num):
        self.__contact_num = num








