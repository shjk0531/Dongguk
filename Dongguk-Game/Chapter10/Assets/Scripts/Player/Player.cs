using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    private Vector3 previousPosition; // ���� ��ġ ����� ����
    public float saveInterval = 1f; // ��ġ ���� ���� (��)

    private float timer; // ��� �ð��� ����ϱ� ���� Ÿ�̸� ����


    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.GetComponent<Enemy>())
        {
            transform.position = previousPosition;
        }
    }


    private void Update()
    {
        timer += Time.deltaTime; // ��� �ð� ����

        if (timer >= saveInterval)
        {
            previousPosition = transform.position; // ���� ��ġ�� ���� ��ġ ������ ����
            timer = 0f; // Ÿ�̸� �ʱ�ȭ
        }
    }
}


