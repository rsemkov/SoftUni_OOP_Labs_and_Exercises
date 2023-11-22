from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_searched = next(x for x in self.categories if x.id == category_id)
        category_searched.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_searched = next(x for x in self.topics if x.id == topic_id)
        topic_searched.topic = new_topic
        topic_searched.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document_searched = next(x for x in self.documents if x.id == document_id)
        document_searched.file_name = new_file_name

    def delete_category(self, category_id):
        category_searched = next(x for x in self.categories if x.id == category_id)
        self.categories.remove(category_searched)

    def delete_topic(self, topic_id):
        topic_searched = next(x for x in self.topics if x.id == topic_id)
        self.topics.remove(topic_searched)

    def delete_document(self, document_id):
        document_searched = next(x for x in self.documents if x.id == document_id)
        self.documents.remove(document_searched)

    def get_document(self, document_id):
        document_searched = next(x for x in self.documents if x.id == document_id)
        return document_searched

    def __repr__(self):
        result = [str(x) for x in self.documents]
        return '\n'.join(result)

