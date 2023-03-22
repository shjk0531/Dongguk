using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// �浹�ϸ� ������ �����Ѵ�
public class OnCollision_StopGame : MonoBehaviour
{

    public string targetObjectName; // ��ǥ ������Ʈ �̸�: Inspector�� ����

    // Start is called before the first frame update
    void Start()    // ó���� �����Ѵ�
    {
        // �ð��� �����δ�
        Time.timeScale = 1.0f;
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        // ���� �浹�� ���� �̸��� ��ǥ ������Ʈ���ٸ�
        if (collision.gameObject.name == targetObjectName)
        {
            // �ð��� �����
            Time.timeScale = 0;
        }
    }
}
