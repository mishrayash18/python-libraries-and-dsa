"basemodel is the foundational class that is used to define, parse"
"and validate datastructures"

"basemodel simplifies the class strucuture as it eliminates manual"
"effort of creating def__init__ functions and other manual effort"
"used in traditional python oop"
# from pydantic import BaseModel, ValidationError
# from typing import Optional
# class info(BaseModel):
#     id:int
#     name: str
#     email: str
#     age: Optional[int] = None
    
# try:
#     user1 = info(id=101, name="yash", email="yash@stu.upes.ac.in")
#     user2 = info(id=102, name="naini", email="naini@stu.in", age=14)
#     print(user1.model_dump()) #converts user1 to a dict
#     print(user2.model_dump())
# except ValidationError as e:
#     print("wrong datatype")




"field--this feature allows the user to add extra boundaries to the data in"
"the basemodel class apart from only specifying the type using typehinting"
# from typing import Optional
# from pydantic import BaseModel, Field, ValidationError

# class employee(BaseModel):
#     # id:int = Field(..., gt=0, lt=200)  #... stands for required parameter
#     id:int = Field(default=1, gt=0, lt=200)
#     """ default fills this parameter automatically and theres no need to 
#     define during object creation"""
#     name:str = Field(min_length=2, max_length=20, description="name of the emp")
#     """description is used for reference to a llm or a tool that would know
#     what the parameter stands for"""
#     email:str = Field(pattern=r"[a-z]+@[a-z]+\.[a-z]+")
#     phone:str = Field(pattern=r"[0-9]{2}-[0-9]{10}")
#     salary:Optional[int] = Field(default=None, gt=0)

# try:
#     e1 = employee(name="yash", email="yash@gmail.com", phone="91-9713223040")
#     print(e1.model_dump())
# except ValidationError as e:
#     print("validation error/ wrong datatype")




"validators - they are custom validation functions that run automatically"
"whenever the user creates a object"
"unlike the usual lt, gt, minlength, maxlength functions validators are used"
"to create functions that have custom python logic"

# from pydantic import BaseModel, Field, field_validator, ValidationError
# class authormetrics(BaseModel):
#     name:str = Field(..., description="name of the author")
#     email:str = Field(..., description="email of the author")
#     commit_cnt:int = Field(..., description="number of commits")
#     insertions:int = Field(..., description="total number of insertions")
#     deletions:int = Field(..., description="total number of deletions")
    
#     @field_validator('commit_cnt')
#     @classmethod
#     #class method refers directly to the class, if it is not satisfied,
#     #the object is not created in the first hand
#     def validate_cmt_cnt(cls, value:int) -> int:
#         if value<0:
#             raise ValueError("commit count cannot be less than 0")
#         return value
# try:
#     user1 = authormetrics(name="yash",
#                         email="yash@gmail.com",
#                         commit_cnt=-2,
#                         insertions=6,
#                         deletions=2)
#     print(user1.commit_cnt)
# except ValidationError as e:
#     print("validation error")




"property- In Python, a property (created using the @property decorator) is"
"a special method that behaves exactly like a regular variable attribute,"
"but executes actual code logic under the hood when accessed.It allows you"
"to calculate data dynamically on demand without having to store redundant"
"values inside your memory."

# from pydantic import BaseModel, Field
# class authormetrics(BaseModel):
#     name:str = Field(..., description="author name")
#     email:str = Field(..., description="author email")
#     commit_cnt:int = Field(default=0, description="number of commits")
#     insertions:int = Field(default=0, description="number of lines inserted")
#     deletions:int = Field(default=0, description="number of lines deleted")

#     @property
#     def cmtcnt(self) -> int:
#         return self.commit_cnt
    
#     @property
#     def modifications(self) -> int:
#         return self.insertions-self.deletions
    
# user1 = authormetrics(name="yash", email="yash@gmail.com", commit_cnt=2,
#                       insertions=6, deletions=3)

# print(user1.cmtcnt)
# print(user1.modifications)



"practice schema"
# from pydantic import BaseModel, Field, field_validator, ValidationError
# class CommitImpact(BaseModel):
#     commit_hash:str = Field(..., description="commit hash")
#     message:str = Field(..., description="message")
#     insertions:int = Field(default=0, description="total number of unsertions")
#     deletions:int = Field(default=0, description="total number of deletions")
    
#     @field_validator('message')
#     @classmethod
#     def cleanspaces(cls, value:str) -> str:
#         cleaned_value = value.strip()
#         if not cleaned_value:
#             raise ValueError("commit message cannot be empty")
        
#         return cleaned_value
        
#     @property
#     def impact_score(self) -> int:
#         return self.insertions+self.deletions
    
# try:
#     user1 = CommitImpact(commit_hash="A",
#                          message="  message",
#                          insertions=3,
#                          deletions=2)
#     print(user1.message)
# except ValidationError as e:
#     print("validation error/wrong datatype")




"model validators- used to review the whole object as one"
# from pydantic import BaseModel, Field, model_validator, ValidationError
# from datetime import datetime
# class ContributionTimeline(BaseModel):
#     name:str = Field(..., description="author name")
#     firstcmtdate:datetime = Field(..., description="first commit date")
#     lastcmtdate:datetime = Field(..., description="last commit date")

#     @model_validator(mode='after')
#     def validcontributions(self) -> "ContributionTimeline":
#         if self.lastcmtdate<self.firstcmtdate:
#             raise ValueError("first commit date " \
#             "cannot be before last commit date")
        
#         return self
    
# try:
#     user1 = ContributionTimeline(name="yash", firstcmtdate=(18, 6, 26), lastcmtdate=(19, 6, 26))
#     print(user1.validcontributions)
# except ValidationError as e:
#     print("validation error")



"practice schema"
# from pydantic import BaseModel, Field, model_validator, ValidationError

# class CommitImpact(BaseModel):
#     name: str = Field(..., description="name of the author")
#     insertions: int = Field(..., description="number of insertions")
#     deletions: int = Field(..., description="number of deletions")

#     @model_validator(mode='after')
#     def validate_total_changes(self) -> "CommitImpact":
#         if self.insertions + self.deletions < 1:
#             raise ValueError("No changes made in this commit (insertions and deletions cannot both be 0)")
#         return self

# # FIX: Moved completely to the left margin out of the class block
# try:
#     user1 = CommitImpact(name="yash", insertions=0, deletions=0)
#     # Pydantic automatically ran your validator! If it succeeds, it reaches here:
#     print(f"Commit safely recorded for: {user1.name}")
    
# except ValidationError as e:
#     print("Validation error successfully triggered and caught!")
#     print(e)
  