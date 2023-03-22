using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Forever_Escape : MonoBehaviour
{
    public string targetObjectName; // ��ǥ ������Ʈ �̸�: Inspector�� ����
    public float speed = 1;         // �ӵ�: Inspector�� ����

    GameObject targetObject;
    Rigidbody2D rbody;

    // Start is called before the first frame update
    void Start()    // ó���� �����Ѵ�.
    {
        // ��ǥ ������Ʈ�� ã�Ƴ���
        targetObject = GameObject.Find(targetObjectName);
        // �߷��� 0���� �ؼ� �浹 �ÿ� ȸ����Ű�� �ʴ´�
        rbody = GetComponent<Rigidbody2D>();
        rbody.gravityScale = 0;
        rbody.constraints = RigidbodyConstraints2D.FreezeRotation;
    }

    private void FixedUpdate()  // ��� �����Ѵ�(���� �ð�����)
    {
        // ��ǥ ������Ʈ�� ������ �����ؼ�
        Vector3 dir = (targetObject.transform.position - this.transform.position).normalized;
        // �� ���⿡ ������ ������ ���ư���
        float vx = dir.x * -speed;
        float vy = dir.y * -speed;
        rbody.velocity = new Vector2(vx, vy);
        // �̵� ���⿡�� ���� ���������� ������ �ٲ۴�
        this.GetComponent<SpriteRenderer>().flipX = (vx < 0);
    }
}
