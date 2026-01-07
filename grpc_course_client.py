import grpc

import course_service_pb2
import course_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))
print(f"Course ID: {response.course_id}")
print(f"Title: {response.title}")
print(f"Description: {response.description}")
