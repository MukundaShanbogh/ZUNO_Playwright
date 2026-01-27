import random
import time

from forty_two_AI.API_assesment.conftest import api_context


class Test_assessment:
    phone_number = "9658664776"

    def send_otp(self,api_context):
        response = api_context.post(
            "/api/v1/auth//otp/send?mode=counselling",
            data={"phoneNumber": f"91{self.phone_number}"}
        )

        body = response.json()
        return body["berry"]

    def verify_otp(self,berry,api_context):
        response = api_context.post(
            "/api/v1/auth//otp/verify?mode=counselling",
        data= {
            "hash":f"{berry}",
            'isValidReq':1,
            'otp':"1111",
            'phoneNumber':f"91{self.phone_number}"
        })
        body = response.json()
        result =  body["result"]
        token = result["token"]
        return token

    def get_questions(self, api_context, token):
        res = api_context.get(
            "/api/v1/counselling/student/pshycometry/test",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert res.status == 200
        body = res.json()
        test_id = body[0]["test_id"]
        attempt_question_ids = [item["attempt_question_id"] for item in body]
        return  test_id,attempt_question_ids



    def submit_answer(self, api_context, token, question_ids, answer_id,test_id,is_submit=False):
        try:
            res = api_context.post(
                "/api/v1/counselling/student/pshycometry/test/submit",
                headers={"Authorization": f"Bearer {token}"},
                data={
                    "attempt_question_id": question_ids,
                    "answer_id": answer_id,
                    "test_id": test_id,
                    "is_submit": is_submit
                })
            assert res.status == 200, f"{res.status} | {res.text}"
        except Exception as e:
            print(f"this is for submit_answer function {e}")
            return None



    def test_token(self,api_context):
        berry  = self.send_otp(api_context)
        token = self.verify_otp(berry,api_context)
        test_id,question_id=self.get_questions(api_context,token)
        for i, qid in enumerate(question_id):
            random_answer_id = random.choice([1, 2, 3, 4])
            is_last = (i == len(question_id) - 1)
            self.submit_answer(
                api_context=api_context,
                token=token,
                question_ids= qid,
                answer_id=random_answer_id,
                test_id=test_id,
                is_submit = is_last
            )










