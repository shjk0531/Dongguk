using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// �浹�ϸ� �����
public class OnCollision_Hide : MonoBehaviour
{

    public string targetObjectName; // ��ǥ ������Ʈ �̸�: Inspector�� ����
    public string hideObjectName;   // ���� ������Ʈ �̸�: Inspector�� ����

    // Start is called before the first frame update
    void Start()    // ó���� �ƹ��͵� ���� �ʴ´�
    {
        
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        // ���� �浹�� ���� �̸��� ��ǥ ������Ʈ���ٸ�
        if (collision.gameObject.name == targetObjectName)
        {
            // ���� ������Ʈ�� ã�Ƽ�
            GameObject hideObject = GameObject.Find(hideObjectName);
            hideObject.SetActive(false);
        }
    }
}
