import os
import re


def extract_ips_from_file(
    input_path="input.txt", output_path="output_comma.txt"
):
    """input.txt 파일을 읽어 서브넷 마스크(/32 등)를 포함하여 IP를 추출한 뒤 쉼표(,)만으로 구분해 저장합니다."""
    # 1. 입력 파일 존재 여부 확인
    if not os.path.exists(input_path):
        print(f"❌ '{input_path}' 파일이 없습니다!")
        print(
            f"   파이썬 파일과 같은 폴더에 '{input_path}' 파일을 만들어 원본 데이터를 넣어주세요."
        )
        return

    # 2. 파일 읽기
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 3. IP 주소 및 선택적 서브넷 마스크(/(1~32))까지 포함하는 정규식 패턴
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/[0-9]{1,2})?\b"
    ip_list = re.findall(ip_pattern, content)

    # 4. 쉼표(,)만으로 연결 (공백 없음)
    result = ",".join(ip_list)

    # 5. 결과 파일로 저장
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print("=" * 40)
    print(f"✅ 처리 완료!")
    print(f" - 추출된 IP 개수: {len(ip_list):,}개")
    print(f" - 저장된 파일명  : {output_path}")
    print("=" * 40)


if __name__ == "__main__":
    extract_ips_from_file()