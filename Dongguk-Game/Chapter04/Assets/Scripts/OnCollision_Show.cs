using System.Collections;
using System.Collections.Generic;
using UnityEngine;


// �浹�ϸ� ǥ���Ѵ�
public class OnCollision_Show : MonoBehaviour
{

    public string targetObjectName; // ��ǥ ������Ʈ �̸�: Inspector�� ����
    public string showObjectName;   // ǥ�� ������Ʈ �̸�: Inspector�� ����

    GameObject showObject;

    // Start is called before the first frame update
    void Start()    // ó���� �����Ѵ�
    {
        // ����� ���� ǥ�� ������Ʈ�� ����� �д�
        showObject = GameObject.Find(showObjectName);
        showObject.SetActive(false);    // �����
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        // ���� �浹�� ���� �̸��� ��ǥ ������Ʈ��
        if (collision.gameObject.name == targetObjectName)
        {
            showObject.SetActive(true); // ������ ���� ǥ���Ѵ�
        }
    }
}
