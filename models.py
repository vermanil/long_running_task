from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Task(Base):
    """
    It store task informations
    """
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    task_id = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'filepath': self.task_id,
        }

class FileInfo(Base):
    """
    FileInfo model to store file data
    """
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    file_pointer = Column(String, unique=True) #absolute path to file
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'filepath': self.file_pointer,
        }

engine = create_engine(
    'sqlite:///long_running_task.db')

Base.metadata.create_all(engine)