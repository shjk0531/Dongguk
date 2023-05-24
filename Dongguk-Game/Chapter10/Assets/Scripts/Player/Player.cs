using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    private Vector3 previousPosition; // 이전 위치 저장용 변수
    public float saveInterval = 1f; // 위치 저장 간격 (초)

    private float timer; // 경과 시간을 계산하기 위한 타이머 변수


    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.GetComponent<Enemy>())
        {
            transform.position = previousPosition;
        }
    }


    private void Update()
    {
        timer += Time.deltaTime; // 경과 시간 증가

        if (timer >= saveInterval)
        {
            previousPosition = transform.position; // 현재 위치를 이전 위치 변수에 저장
            timer = 0f; // 타이머 초기화
        }
    }
}


